  
  //Advance Range Slider 
  jQuery(document).ready(function(){
  
    var getOutput    = $("#state");
    var getSlider = $("#advance_slide");
  
    getSlider.slider({
      range:true,
      min:0,
      max:500000,
      values:[0, 500000],
      step:10000,
      slide:function(event, ui){
        getOutput.html( ui.values[0]+' - '+ui.values[1]+'Tk');
        $("#minValue").val(ui.values[0]);
        $("#maxValue").val(ui.values[1]);
      }
    });
    getOutput.html(getSlider.slider("values",0)+' - '+getSlider.slider("values",1)+"Tk");
    $("#minValue").val(getSlider.slider('values', 0));
    $("#maxValue").val(getSlider.slider('values', 1));
  
  });