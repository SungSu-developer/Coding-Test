import yt_dlp
 
# 테스트하고 싶은 유튜브 영상 주소 (여기에 URL을 넣으세요)
# 예시: 짧은 애니메이션이나 뉴스 클립 추천
# video_url = 'https://www.youtube.com/watch?v=bxMQi3h_VUI' 
# video_url = "https://www.youtube.com/watch?v=SuzOFaQ4ZRI"
video_url = "https://www.youtube.com/watch?v=MezvFK_r-MI"
 
# 다운로드 설정
ydl_opts = {
    'format': 'best[ext=mp4]',  # mp4 형식 중 화질 좋은 것
    'outtmpl': '/Users/sspto/music1.mp4', # 저장될 파일명 지정 (중요!)
    'quiet': True,              # 불필요한 로그 숨김
    'no_warnings': True,
}
 
print("📥 영상 다운로드를 시작합니다... (잠시만 기다려주세요)")
 
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("✅ 다운로드 완료! 'sky1_video.mp4' 파일이 생성되었습니다.")
except Exception as e:
    print(f"❌ 오류 발생: {e}")