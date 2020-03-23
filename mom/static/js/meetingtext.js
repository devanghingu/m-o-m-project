let meeting_text, note_text, note;
let edit_item_btn = "<div style='text-align:right;'>" +
"<a href='javascript:void(0);' id='edit_note_btn' class='btn btn-primary btn-sm'><i class='fa fa-fw fa-pencil-alt'></i></a>&nbsp;"+
"<a href='javascript:void(0);' id='remove_note_btn' class='btn btn-danger btn-sm'><i class='fas fa-trash-alt'></i></a>" +
"</div>";

function edit_item_can_btn() {
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick', 'showButton(event)');
}

function getSelectedText(e) {   //this is call when we click on show button(add to note) button
   selectedtext = "";
   if (window.getSelection().toString().length > 7) {
      selectedtext = window.getSelection().toString();
      
      newli = $(document.createElement('li'));
      newli.addClass('list-group-item');
      newli.addClass('note-li');
      newli.attr('draggable', 'true');
      newli.attr('role', 'option');
      newli.attr('aria-grabbed', 'false');
      var key = Object.keys(notes);
      var len = key.length;
      if(len>0){    
         notes[parseInt(key[len-1])+1] = selectedtext; // if Dictionary has value then assign value on last key+1 of note
         newli.attr('dict_id',parseInt(key[len-1])+1); //If Dictionary has value then assign value on last key+1 of note 
      }else{ 
         notes[1]=selectedtext; // if Dictionary is empty then Assign value on 1 key of note  
         newli.attr('dict_id',parseInt(key[len-1])+1)
      }
      newli.html(selectedtext + edit_item_btn);
      $('.sortable').append(newli);
   }
}
function showButton(e) {  //when we select the first time this call
   e.stopPropagation();
   var meetingtext = document.getElementById("meetingtext");
   var tar = e.target.getBoundingClientRect();
   if (window.getSelection().toString().length >= 8) {
      $('.showbtn').css({ top: 8 + e.clientY, left: 12 + e.clientX }).show();
   }
   else {
      $('.showbtn').hide();
   }
}
$(document).on("click", function (e) {
   e.stopPropagation();
   $('.showbtn').hide();
});

$(document).ready(function () {  
 
   for(id in notes){
      newli = $(document.createElement('li'));
      newli.addClass('list-group-item');
      newli.addClass('note-li');
      newli.attr('draggable', 'true');
      newli.attr('role', 'option');
      newli.attr('aria-grabbed', 'false');
      newli.attr('dict_id', id);
      newli.html(notes[id] + edit_item_btn);
      $('.sortable').append(newli);
   }
});
function expandtextarea(e) {
   if ($('#meeting-textarea')[0].scrollTop != 0) {
      $('#meeting-textarea').height($('#meeting-textarea')[0].scrollHeight);
   }
}

function expandtextarea_note(e) {
   if ($('#note-textarea')[0].scrollTop != 0) {
      $('#note-textarea').height($('#note-textarea')[0].scrollHeight);
   }
}
function edit_meeting_save_btn() {
   var meeting_text = $('#meeting-textarea').val();
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick', 'showButton(event)');
   
}

function edit_meeting_can_btn() {
   $('#meetingtext').html(meeting_text);
   $('#meetingtext').attr('onclick', 'showButton(event)');
   
}


let note_textarea = "<div style='margin-top:5px;text-align:right;'>" +
   "<button type='button' id='note_save_btn' class='btn btn-primary btn-sm'><i class='fa fa-fw fa-check'></i></button> &nbsp;" +
   "<button type='button' id='note_can_btn' class='btn btn-danger btn-sm'><i class='fa fa-fw fa-times'></i></button></div>";
$(document).on('click', 'a#edit_note_btn', function () {
   var note = $(this).closest('li');
   note_text = note.text();
   var textarea = "<div style='float:left;'><textarea class='form-control input-large' id='note-textarea' onkeypress='expandtextarea_note(event)' placeholder='you can add new content' wrap='hard'  cols='110'></textarea></div>";
   note.html(textarea + note_textarea);
   $('#note-textarea').height($('#note-textarea')[0].scrollHeight);
   $('#note-textarea').val(note_text);

   $('a#edit_note_btn').prop('disabled', true);
   $('#meetingtext').removeAttr('onclick');
});

$(document).on('click', 'a#remove_note_btn', function () {
   $(this).closest('li').remove();
   delete notes[$(this).closest('li').attr('dict_id')]
});

$(document).on('click', 'button#note_save_btn', function () {
   var note = $(this).closest('li');
   note.html($('#note-textarea').val() + edit_item_btn);
   notes[note.attr('dict_id')]=note.text()
   $('a#edit_note_btn').prop('disabled', false);
   $('#meetingtext').attr('onclick', 'showButton(event)');
});

$(document).on('click', 'button#note_can_btn', function () {
   var note = $(this).closest('li');
   note.html(note_text + edit_item_btn);
   $('a#edit_note_btn').prop('disabled', false);
   $('#meetingtext').attr('onclick', 'showButton(event)');
});

$('#done').click(function (){
   // $("input[name=meetingtext]").attr('value',$("#meetingtext").html())
   $("input[name=meetingtext]").val($("#meetingtext").html());
   $("#meetingtnote").attr('value',JSON.stringify(notes)) 
});