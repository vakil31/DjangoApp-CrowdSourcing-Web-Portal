var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton = document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton = document.getElementById("submitBtn");
var a = document.getElementById("scorelink");
var vidId = document.getElementById("videoid")
const param = new URLSearchParams(location.search);
var i = 0;
var score = 0;
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');
var data_single = {
  'csrfmiddlewaretoken': csrftoken,
  'score': score
}
var files = {};
//Selecting Videos
function readFiles(event) {
  files = document.getElementById("file").files;
  //data_single['fileName'] = files[i].name;
  loadAsUrl(files[i]);
}
//Generating csrf token for POST operation
//Data to POST
//Function called after viewing all videos
function updateScore_single() {
  $.ajax({
    url: "/videoplay/videos/",
    type: "POST",
    //dataType: "json",
    data: data_single,
    success: function (json) {
      //console.log(files[i].name);
      loadAsUrl(files[i]);
    },
    error: function (xhr, errmsg, err) {
      alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
    }
  });
}
//Score slider
slider.oninput = function () {
  output.innerHTML = this.value;
  score = this.value;
  data_single['score'] = score;
}
//To go to next video:'Submit Score' button
function disableScroll() {
  submitButton.hidden = true;
  slider.hidden = true;
  slider.style.opacity = 0.2;
  slider.disabled = true;
}
//Series of events after video ends
myVideo.addEventListener('ended', enableDisablebuttons, false);
function enableDisablebuttons(e) {
  slider.value = 50;
  output.innerHTML = 50;
  slider.style.opacity = 0.8;
  slider.disabled = false;
  slider.hidden = false;
  myVideo.style.display = "none";
  playButton.style.display = "none";
  selVideo[0].style.display = "none";
  submitButton.hidden = false;
  i++;
  document.getElementById("scoreDisp").hidden = false;
  document.exitFullscreen();
}
//Loading the video files
function loadAsUrl(theFile) {
  var reader = new FileReader();
  reader.onload = function (loadedEvent) {
    myVideo.setAttribute("src", loadedEvent.target.result);

  }
  reader.readAsDataURL(theFile);
}
//Play the videos
function playVid() {
  if (i > 0) {
    console.log("In playVid ");
    data_single['score'] = JSON.stringify(data_single['score'])
    data_single['fileName'] = files[i-1].name;
    updateScore_single();
    submitButton.hidden = true;
    slider.hidden = true;
    slider.style.opacity = 0.2;
    slider.disabled = true;
    myVideo.autoplay = true;
  }
  if (i == files.length) {
    window.location.href = "/videoplay/temp/"
  }
  myVideo.style.display = "block";
  playButton.style.display = "none";
  myVideo.play();
  console.log(i);

}
// //Change to full screen
function toggleFullscreen() {
  console.log("Toggle Screen");
  if (myVideo.paused) {
    if (myVideo.requestFullscreen) {
      myVideo.requestFullscreen();
    }
    else if (myVideo.mozRequestFullScreen) {
      myVideo.mozRequestFullScreen();
    }
    else if (myVideo.webkitRequestFullScreen) {
      myVideo.webkitRequestFullScreen();
    }
    else if (myVideo.msRequestFullscreen) {
      myVideo.msRequestFullscreen();
    }
    playVid();
  }
  else {
    document.exitFullscreen();
  }
  myVideo.style.display = "block";
  console.log(i);

}
//Pause Video
function pauseVid() {
  myVideo.pause();
}
//Just to make sure static files are connected, see this message in console
console.log("Hello! Static Cnnected");
