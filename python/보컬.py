import pretty_midi
import numpy as np

def find_vocal_track_auto(midi_file_path):
    try:
        # 1. MIDI 파일 로드
        midi_data = pretty_midi.PrettyMIDI(midi_file_path)
        print(f"📂 파일 분석 중: {midi_file_path}\n")
        
        candidates = []

        print(f"{'Track':<6} | {'악기 이름':<15} | {'노트 수':<7} | {'겹침(화음)%':<10} | {'평균 음정':<10} | {'판정'}")
        print("-" * 75)

        for i, instrument in enumerate(midi_data.instruments):
            # 드럼 트랙은 무조건 제외 (is_drum 속성 활용)
            if instrument.is_drum:
                print(f"Trk {i:<2} | (Drums)         | {len(instrument.notes):<7} | -          | -          | 🥁 드럼")
                continue
                
            # 노트가 너무 적으면(50개 미만) 보컬 아님 (효과음일 확률)
            if len(instrument.notes) < 50:
                print(f"Trk {i:<2} | {instrument.name[:10]:<10} | {len(instrument.notes):<7} | -          | -          | ❌ 너무 짧음")
                continue

            # --- [핵심] 화음 판별 알고리즘 ---
            # 모든 노트를 시간순으로 정렬
            sorted_notes = sorted(instrument.notes, key=lambda x: x.start)
            total_duration = sorted_notes[-1].end - sorted_notes[0].start
            overlap_duration = 0
            
            # 앞 노트가 끝나기 전에 뒷 노트가 시작되면 '겹침'으로 간주
            for j in range(len(sorted_notes) - 1):
                curr_note = sorted_notes[j]
                next_note = sorted_notes[j+1]
                
                # 0.05초 이상의 겹침만 인정 (미세한 연주 오차는 무시)
                if curr_note.end > next_note.start + 0.05:
                    overlap = min(curr_note.end, next_note.end) - next_note.start
                    overlap_duration += overlap

            # 겹침 비율 (0.0 = 완전 단음/보컬, 0.5 = 절반이 화음/피아노)
            polyphony_rate = overlap_duration / total_duration if total_duration > 0 else 0
            
            # --- [핵심] 음역대 확인 ---
            pitches = [n.pitch for n in instrument.notes]
            avg_pitch = np.mean(pitches) # 60=가온다 (보통 보컬은 45~85 사이)

            # 판정 로직
            is_vocal_candidate = False
            type_str = ""
            
            if polyphony_rate > 0.1: # 10% 이상 겹치면 반주 악기
                type_str = "🎹 악기(화음)"
            elif avg_pitch < 40:     # 너무 낮으면 베이스
                type_str = "🎸 베이스"
            else:
                type_str = "🎤 보컬 후보!"
                is_vocal_candidate = True

            # 결과 출력
            print(f"Trk {i:<2} | {instrument.name[:10]:<10} | {len(instrument.notes):<7} | {polyphony_rate*100:5.1f}%     | {avg_pitch:5.1f}      | {type_str}")

            if is_vocal_candidate:
                # 점수 계산: 화음이 적을수록(+), 노트가 많을수록(+)
                score = (1 - polyphony_rate) * 100 + (len(instrument.notes) / 100)
                candidates.append((i, score, instrument))

        print("-" * 75)

        # 가장 유력한 트랙 선정
        if candidates:
            best_track = max(candidates, key=lambda item: item[1]) # 점수 1등 찾기
            print(f"\n🏆 최종 결론: Track {best_track[0]}번이 '보컬(멜로디)' 입니다!")
            return best_track[0], best_track[2]
        else:
            print("\n❌ 보컬 트랙을 찾지 못했습니다. (모두 반주 트랙 같습니다)")
            return None, None

    except Exception as e:
        print(f"오류 발생: {e}")
        return None, None

# --- 실행 ---
# '케데헌 골든' 파일 경로를 넣고 돌려보세요
best_track_id, best_track_data = find_vocal_track_auto("케데헌 골든_midiex.net_pre_.mid")