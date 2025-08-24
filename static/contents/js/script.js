// 공유 버튼 기능
function copyLink(link) {
  navigator.clipboard.writeText(link);
  alert("복사됨: " + link);
}

// 가장 화면 중앙에 가까운 영상만 재생
function playClosestVideo() {
  const videos = document.querySelectorAll("video");
  let closest = null;
  let closestDist = Infinity;

  videos.forEach(video => {
    const rect = video.getBoundingClientRect();
    const videoCenter = rect.top + rect.height / 2;
    const screenCenter = window.innerHeight / 2;
    const dist = Math.abs(videoCenter - screenCenter);

    if (dist < closestDist) {
      closestDist = dist;
      closest = video;
    }
  });

  videos.forEach(video => {
    if (video === closest) {
      video.play().catch(() => {});
    } else {
      video.pause();
    }
  });
}

// IntersectionObserver
const observer = new IntersectionObserver(() => {
  playClosestVideo();
}, { threshold: 0.5 });

document.addEventListener("DOMContentLoaded", () => {
  const videos = document.querySelectorAll("video");
  videos.forEach(video => observer.observe(video));
  playClosestVideo(); // 첫 로딩 시 실행
});
