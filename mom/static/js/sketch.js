//(function(){
  
let mic, fft,level1,state,soundFile,recorder;
let can1;
var timer=null;

/** first setup the microphone **/
function setup() {
  state=0;
  window.onbeforeunload = null;
  can1=createCanvas(400, 400);
  can1.parent('canvas-area');
  noFill();
  mic = new p5.AudioIn();
  mic.start(); //start mic
  fft = new p5.FFT();
  fft.setInput(mic);  
}

/** when mic on draw the circle on canvas **/
function draw() {
  background(245, 247, 250);
  let spectrum = fft.analyze();
  // strokeWeight(2);
  stroke(61, 191, 232);
  beginShape();
  if(state==1){
    nanoel=ellipse(200,200,50,50);
    for (i = 0; i < spectrum.length; i++) {

      w=spectrum[i]<50?spectrum[i]+30:50;
      y=spectrum[i]<50?spectrum[i]+30:50;
      ellipse(200,200,100+spectrum[i],100+spectrum[i]);  
    }
    endShape();
  }else if($('#record-meeting').text()=='Resume'){
    textSize(32);
    text("Resume Recordering",40,180)
  }else{
    textSize(32);
    text("Click To Start Meeting",40,180)
  }
}

/** variable for count request and response **/
let response_text;
let response_counter,request_counter;


/** run following code when documnet is ready **/
$(document).ready(function(){
  
  /** do get request for check server response **/
  CheckServerResponse();

  /**  Start Meeting button and Resume button **/
  $('#record-meeting').click(function(){
    
      if (state === 0 && mic.enabled){
          getAudioContext().resume()
          recorder = new p5.SoundRecorder();
          recorder.setInput(mic);
          soundFile = new p5.SoundFile();
          recorder.record(soundFile);
          console.log("play")
          $(this).text('Pause')
          $('#stop').removeAttr('hidden');
          state=1;
          request_counter=0;
          response_counter=0;
          response_text=[];
          timer=setTimeout(sendajexrequest,60000)
      }else{
          /** Pause button send the data in server **/
          recorder.stop(); 
          AjaxRequest();
          state=0;
          console.log("pause")
          $(this).text('Resume');

          if(timer)
          {
            clearTimeout(timer); //cancel the previous timer.
            timer = null;
          }
      }
  });
  
  /** Stop button send the data in server **/
  $("#stop").click(function(){
    
    if(state==1 && $("#record-meeting").text()=='Pause'){
      recorder.stop(); 
      console.log("after Stop")
      AjaxRequest()
      $('#record-meeting').prop('disabled','false');
    }
    $(this).attr('hidden','true');
    $('#record-meeting').html('Start Meeting')
    state=0;
    if(timer)
    {
      clearTimeout(timer); //cancel the previous timer.
      timer = null;
    }
    $('#loader-audio').removeAttr('hidden');
    $('#canvas-area').hide();
    $('#record-meeting').prop('disabled','true');
  });
  
});
/** document ready code close here **/

/** do get request when the page is load **/
function CheckServerResponse(){
  
  $.ajax({
    url:'http://3.6.222.183:8000',
    method:'get',  
    dataType:'json',
    processData: false,
    contentType:false,
    success:function(data){
     
    },
    error: function(){
      $('#record-message').html("<u>Opps..!!</u> <b>M-O-M is down right now.</b> contact administrator for more.!!!");
      $('#loader-audio').removeAttr('hidden');
      $('#record-meeting').prop('disabled','true');
      $('#canvas-area').hide();
    },
    timeout:5000
  });
}

/** send ajex request using after one minute send request to server **/
function sendajexrequest(){
  console.log('60 sec')
  timer=setTimeout(sendajexrequest,60000)  
  recorder.stop(); 
  AjaxRequest();
  getAudioContext().resume()
  recorder = new p5.SoundRecorder();
  recorder.setInput(mic);
  soundFile = new p5.SoundFile();
  recorder.record(soundFile);
}

/** do Ajex request when pause and stop button click  **/
function AjaxRequest(){
  var form = new FormData();
  form.append('wavfile',soundFile.getBlob(),'file');
  request_counter+=1;
  try{
    $.ajax({
    
      url:'http://3.6.222.183:8000',
      method:'POST',
      data:form,  
      dataType:'json',
      processData: false,
      contentType:false,
      success:function(data){
          response_text.push(data['data'])
          response_counter+=1;
          if(request_counter==response_counter && state==0 ){
              $('#loader-audio').attr('hidden','true');
              $('#canvas-area').show();
              $('#record-meeting').removeAttr('disabled');
              localStorage.setItem('response_text',JSON.stringify({"response_text":response_text}));
              window.location.replace('/meetingtext');
            }
        },
    });
  }catch(error){
    $('#loader-audio').removeAttr('hidden');
    $('#record-message').text("Server Does Not Response")
  } 
}

/** Prevent to reload and close before alert **/
window.onbeforeunload = function(){
  console.log('hello----d')
  return 'Are you sure you want to leave?';
};
//})();