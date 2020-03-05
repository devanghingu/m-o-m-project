let edit_item_btn;
let meeting_text, note_text,note;

function edit_item_can_btn(){ 
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick','showButton(event)');
   $("#edit-meeting-btn").prop('disabled',false);
}

function getSelectedText(e)
{
   selectedtext="";
   if(window.getSelection().toString().length>7)
   {
      selectedtext = window.getSelection().toString();
      edit_item_btn =  "<div style='text-align:right;'>"+
      "<a href='javascript:void(0);' id='edit_note_btn' class='btn btn-primary btn-sm'><i class='fa fa-fw fa-pencil-alt'></i></a> &nbsp;"+
      "<a href='javascript:void(0);' id='remove_note_btn' class='btn btn-info btn-sm'><i class='fa fa-fw fa-times'></i></a>"+
      "</div>";
      newli=$(document.createElement('li'));
      newli.addClass('list-group-item');
      newli.addClass('note-li');
      newli.attr('draggable','true');
      newli.attr('role','option');
      newli.attr('aria-grabbed','false');
      newli.html(selectedtext+edit_item_btn);
      $('.sortable').append(newli);
   }
}
function showButton(e){
   e.stopPropagation();
   var meetingtext=document.getElementById("meetingtext");
   var tar = e.target.getBoundingClientRect();
   if(window.getSelection().toString().length >=8 )
   {
      $('.showbtn').css({ top : 8+ e.clientY, left : 12+e.clientX}).show();
   }
   else{
      $('.showbtn').hide();
   }
}
$(document).on("click", function(e) {
   e.stopPropagation();
   $('.showbtn').hide();
});
$('#done').click(function(){
   note = [];
   $('.sortable').each(function(){
      $(this).find('li').each(function(){
         note.push($(this).text());
      });
   });
});

$(document).ready(function(){
   $('#edit-meeting-btn').click(function(){
      meeting_text = $('#meetingtext').text();
      var textarea = "<textarea class='form-control input-large' id='meeting-textarea' onkeypress='expandtextarea(event)' placeholder='you can add new content' wrap='hard'  cols='110'></textarea>" +
      "<div class='editable-buttons editable-buttons-bottom' style='margin-top:5px;'>"+
      "<button type='button' id='edit-meeting-save-btn' class='btn btn-primary btn-sm' onclick='edit_meeting_save_btn()'><i class='fa fa-fw fa-check'></i></button> &nbsp;"+
      "<button type='button' id='edit-meeting-can-btn' class='btn btn-info btn-sm' onclick='edit_meeting_can_btn()'><i class='fa fa-fw fa-times'></i></button></div>";

      $('#meetingtext').removeAttr('onclick'); 
      $('#meetingtext').html(textarea);
      $('#meeting-textarea').val(meeting_text);
      $('#meeting-textarea').height($('#meeting-textarea')[0].scrollHeight);
      $("#edit-meeting-btn").prop('disabled',true);
   });
});
function expandtextarea(e){
      if($('#meeting-textarea')[0].scrollTop != 0)
      {
         $('#meeting-textarea').height($('#meeting-textarea')[0].scrollHeight);
      }
}

function expandtextarea_note(e){
      if($('#note-textarea')[0].scrollTop != 0)
      {
         $('#note-textarea').height($('#note-textarea')[0].scrollHeight);
      }
}
function edit_meeting_save_btn(){
   var meeting_text = $('#meeting-textarea').val();
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick','showButton(event)');
   $("#edit-meeting-btn").prop('disabled',false);
}

function edit_meeting_can_btn(){ 
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick','showButton(event)');
   $("#edit-meeting-btn").prop('disabled',false);
}


let note_textarea ="<div style='margin-top:5px;text-align:right;'>"+
"<button type='button' id='note_save_btn' class='btn btn-primary btn-sm'><i class='fa fa-fw fa-check'></i></button> &nbsp;"+
"<button type='button' id='note_can_btn' class='btn btn-info btn-sm'><i class='fa fa-fw fa-times'></i></button></div>";
$(document).on('click','a#edit_note_btn',function(){
   var note = $(this).closest('li');
   note_text=note.text();
   var textarea = "<div style='float:left;'><textarea class='form-control input-large' id='note-textarea' onkeypress='expandtextarea_note(event)' placeholder='you can add new content' wrap='hard'  cols='110'></textarea></div>"; 
   note.html(textarea+note_textarea);
   $('#note-textarea').height($('#note-textarea')[0].scrollHeight);
   $('#note-textarea').val(note_text);

   $('a#edit_note_btn').prop('disabled', true);
   $("#edit-meeting-btn").prop('disabled',true);
   $('#meetingtext').removeAttr('onclick'); 
});

$(document).on('click','a#remove_note_btn',function(){
   $(this).closest('li').remove();
});

$(document).on('click','button#note_save_btn',function(){
   var note = $(this).closest('li');
   note.html($('#note-textarea').val()+edit_item_btn);
   $('a#edit_note_btn').prop('disabled',false);
   $("#edit-meeting-btn").prop('disabled',false);
   $('#meetingtext').attr('onclick','showButton(event)');
});

$(document).on('click','button#note_can_btn',function(){
   var note = $(this).closest('li');
   note.html(note_text+edit_item_btn);
   $('a#edit_note_btn').prop('disabled',false); 
   $("#edit-meeting-btn").prop('disabled',false);
   $('#meetingtext').attr('onclick','showButton(event)');
});