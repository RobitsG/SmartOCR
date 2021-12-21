document.body.innerHTML += ('<div id="preloader-body"><div id="cube-wrapper"><div class="cube-folding"><span class="leaf1"></span><span class="leaf2"></span><span class="leaf3"></span><span class="leaf4"></span></div><span class="loading"data-name="Loading">Loading</span></div></div>');
window.onload = function () {
    document.getElementById('cube-wrapper').style.display = "none";
    document.getElementById('preloader-body').style.display = "none";
}