var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
var vidId = document.getElementById("videoid");

const param=new URLSearchParams(location.search);
var i=0;
var score=0;
var start=0;
var vid_pair_num=0;
var name_list=[['1_fps25.mp4','3_fps24.mp4'],['2_fps24.mp4','4_fps25.mp4']]
console.log(name_list.length)
var objs = ["video1","video2"];
for(var i =0;i<objs.length;i++)
{
    console.log("hi");
    var f =  objs[i];
   console.log(f);
}

//document.getElementById('radio1').value = f;
var radiob1 = document.getElementsByName("optradio1");
for (var i = 0, length = radiob1.length; i < length; i++)
{
console.log(radiob1[i]);
}
function preference()
{
// var b1 = document.getElementById('radio1');
// var b2 = document.getElementById('radio2');
console.log("Inside func peference");

//console.log("length is ",radiob1.length);
if(document.getElementById('radio1').checked) {
  //Male radio button is checked
  console.log(radiob1[0].value);
}else if(document.getElementById('radio2').checked) {
  //Female radio button is checked
  console.log(radiob1[1].value);
}

// for (var i = 0, length = radiob1.length; i < length; i++)
// {
// console.log(radiob1[i]);
// if (radiob1[i].checked)
// {
// // do whatever you want with the checked radio
// console.log("yes");
// console.log(radiob1[i].value);
// break;

// // only one radio can be logically checked, don't check the rest

// }
// }

}
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      console.log(cookie)
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

var data = {
  'csrfmiddlewaretoken': csrftoken,
  'score': score
}
var files={};
//Selecting Videos
function readFiles(event) {
  console.log("Inside ReadFile Function")
  files=document.getElementById("file").files;
  data['fileName']=files[i].name;
  console.log(files.length)
  // console.log(data['fileName'])
  // console.log(files[i])
  // loadAsUrl(files[i]);
}

// localStorage.setItem('storeObj', JSON.stringify(myObj));
// console.log(JSON.parse(localStorage.getItem('storeObj')));

//Generating csrf token for POST operation

//Data to POST

//Function called after viewing all videos
function updateScore(){
  $.ajax({
      url: "/videoplay/videos2/",
      type: "POST",
      //dataType: "json",
      data: data,
      success: function (json) {
        //console.log(files[i].name);
        // loadAsUrl(files[i]);
      },
      error: function (xhr, errmsg, err) {
        alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
      }
    });
}


//Score slider
slider.oninput = function() {
  output.innerHTML = this.value;
  score=this.value;
  data['score']=score;
}


//To go to next video:'Submit Score' button
// function nextVid(){
//   //i++;
//   console.log(files[i]);
//   console.log(i);
  
// if (i == 3) {
//   i=0;
//   console.log(score);
//   // updateScore();
// }
// data['score'] = JSON.stringify(data['score'])
// updateScore();
// // loadAsUrl(files[i]);
// slider.value = 50;
// output.innerHTML = 50;
// disableScroll();
// }

// document.addEventListener('fullscreenchange', exitHandler);
// document.addEventListener('webkitfullscreenchange', exitHandler);
// document.addEventListener('mozfullscreenchange', exitHandler);
// document.addEventListener('MSFullscreenChange', exitHandler);

// function exitHandler() {
//   if (!document.fullscreenElement && !document.webkitIsFullScreen && !document.mozFullScreen && !document.msFullscreenElement) {
//     ///fire your event
//    alert("hey");
    
//   }
// }






function disableScroll(){
  submitButton.hidden = true;
  slider.hidden = true;
  slider.style.opacity=0.2;
  slider.disabled=true;
}
var vid_num = 1;
//Series of events after video ends
myVideo.addEventListener('ended', videoloop,false);
/////////////////////////////////////////////////////////


function enableDisablebuttons() {
       slider.style.opacity=0.8;
       slider.disabled=false;
       slider.hidden=true;
       myVideo.style.display = "none";
       playButton.style.display="none";
       selVideo[0].style.display="none";
       submitButton.hidden=false;
       i++;
       document.getElementById("scoreDisp").hidden=false;
       document.exitFullscreen();
}
//Loading the video files
function loadAsUrl(theFile) {
    var reader = new FileReader();
    reader.onload = function(loadedEvent) {
      myVideo.setAttribute("src", loadedEvent.target.result);
        
    }
    reader.readAsDataURL(theFile);
}
//Play the videos
// function playVid(){
//     if(i>0){
//       data['score'] = JSON.stringify(data['score'])
//       data['fileName'] = files[i-1].name;
//       updateScore();
//       submitButton.hidden = true;
//       slider.hidden = true;
//       slider.style.opacity = 0.2;
//       slider.disabled = true;
//       myVideo.autoplay=true;
//     }

//   if(i==files.length){
//     window.location.href="/videoplay/temp/"
//   }
//     myVideo.style.display = "block";
//     playButton.style.display = "none";
//     myVideo.play();
//     console.log(i);
    
//   }

// //Change to full screen
function toggleFullscreen() {
  console.log("Toggle Screen");

  if(myVideo.paused)
  {
    console.log("Video is Paused")
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

    doublestimulus(name_list);

}
   else {
     console.log("Video is not Pause")
    document.exitFullscreen();
  }
    myVideo.style.display="block";
    console.log(i);
    
}
//Pause Video
function pauseVid() {
myVideo.pause();
}

///////////////////////////////////////////////////
function getuploadedpath(vid_name)
{
  for (var i = 0; i < files.length; i++)
  {
    if (files[i].name==vid_name)
    {
      return files[i];
    }
  }
}
///////////////////////////////////////////////////////
function playVid2()
{
  console.log("Inside playVid2")
  submitButton.hidden = true;
  slider.hidden = true;
  slider.style.opacity = 0.2;
  slider.disabled = true;
  myVideo.autoplay=true;
  myVideo.style.display = "block";
  playButton.style.display = "none";
  myVideo.blur();
  myVideo.play();
  console.log("finished playing video")
  return;
}
function delay()
{
  k=0
    while(k<400)
    {
      console.log("Inside Delay loop")
      j=0;
      while(j<1000000)
      {
        j++
      }
      k++;
    }
    return;
}
var pair_end=0;
function doublestimulus(name_list)
{
  console.log("Inside Double Stimulus function")
  // debugger;
  if(vid_pair_num<name_list.length)
  {
    if(vid_num==1){
      console.log("Gonna Play Vid1")
      console.log(name_list[vid_pair_num][0])
      path1 = getuploadedpath(name_list[vid_pair_num][0])
      console.log('path1\n',path1)
      loadAsUrl(path1)
      playVid2();
      vid_num=2
    }
    else{
    console.log("Gonna Play Vid2")
    console.log(name_list[vid_pair_num][1])
    path2 = getuploadedpath(name_list[vid_pair_num][1])
    console.log('path2\n',path2)
    loadAsUrl(path2)
    // await sleep(3000)
    console.log('gonna pause before starting second video')
    delay();  
    playVid2();
    // window.setTimeout(playVid2,3000);
    // window.setTimeout(playVid2,10000)
    vid_num=1
    vid_pair_num+=1;
    pair_end=1;
    // enableDisablebuttons()
    }
    
  }
  else{
    window.location.href="/videoplay/temp/"
  } 
  
  return;
}

function videoloop(e)
{
  console.log("Inside Videoloop")
  // doublestimulus(name_list);
  if(pair_end==1)
  {
    nextpair()
    pair_end=0;
  }
  else{
    doublestimulus(name_list);
  }

}
  // toggleFullscreen();
  // if(vid_num==2)
  // {
  //  console.log("Going to play second video in pair")
  //  console.log(name_list[vid_pair_num][1])
  //  path2 = getuploadedpath(name_list[vid_pair_num][1])
  //  console.log('path2\n',path2)
  //  loadAsUrl(path2)
  //  playVid2();
  //  vid_num=1
  // //  enableDisablebuttons()
  //  return;
  // }
  // else
  // {
  //   console.log("Going to play first video in pair")
  //   doublestimulus(name_list)
  // }
  

  function nextpair()
  {
    enableDisablebuttons()
    //myVideo.style.display="none"
    var preference = prompt("Enter 1 if first video was better else enter 2!");
    data['preference']=preference
    data['preference']=JSON.stringify(data['preference'])
    data['vid_name1']=name_list[vid_pair_num-1][0]
    data['vid_name2']=name_list[vid_pair_num-1][1]
    updateScore();
    // toggleFullscreen()
  }









//Just to make sure static files are connected, see this message in console
console.log("Hello! Static Cnnected");
   