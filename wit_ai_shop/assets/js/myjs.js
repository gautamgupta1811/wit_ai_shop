window.addEventListener("load", initEvent);
var flag = false;

function initEvent() {
    mic_btn = document.querySelector(".microphone");
    mic_btn.addEventListener("click", toggleMic);
}

function toggleMic() {
    if (!flag) {
        mic_btn.innerHTML = '<i class="fa fa-microphone"></i>';
        mic_btn.style.background = "#c21c2f";
    } else {
        mic_btn.innerHTML = '<i class="fa fa-microphone-slash"></i>';
        mic_btn.style.background = "#ff5063";
    }
    flag = !flag;
}