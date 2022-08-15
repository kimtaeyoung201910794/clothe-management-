var keyList_category = Object.keys(dict_category)
var init_select_child

$(document).ready(function(){
    var select_parent = $('#select-parent');

    keyList_category.forEach(function(item) {
        var option_parent = document.createElement('option');
        $(option_parent).val(item);
        $(option_parent).text(item);

        select_parent.append(option_parent);
    });

    $(select_parent).val(cur_parent).prop("selected", true);
    $(select_parent).trigger("change")
    $('#select-child').val(cur_child).prop("selected",true);
    
    var season_labels = $("#position_flex1>label");
    for(var label of season_labels){
        if($(label).text() == cur_season){
            console.log(label)
            $(label).trigger("click")
        }
    }
    var style_labels = $("#position_flex2>label");
    for(var label of style_labels){
        if($(label).text() == cur_style){
            console.log(label)
            $(label).trigger("click")
        }
    }
    var color_inputs = $("#position_flex3>input");
    for(var input of color_inputs){
        
        if($(input).val() == cur_color){
            console.log(input)
            $(input).next().trigger("click")
        }
    }
});

$('#select-parent').change(function(){
    $('#select-child option:gt(0)').remove()
    
    var select_child = $('#select-child');
    var key = $(this).val()
    dict_category[key].forEach(function(item) {
        var option_child = document.createElement('option');
        $(option_child).val(item);
        $(option_child).text(item);

        select_child.append(option_child);
    });

});

$('#btn-img').click(function(){
    $('#form-img').trigger('click');
});

$(function() {
    $("#form-img").on('change', function(){
    readURL(this);
    });
});
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
        $('#input_img').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}