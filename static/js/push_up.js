function push_up_start() {
    $('.bg').css("display", "none");
    $('.숫자보여지는 화면').show();
    console.log($("#max_num").val())
    $.ajax({
        type: "GET",
        url: "/push_up/set_play",
        data: {
            'max_num_give': $("#max_num").val(),
            'min_num_give': $("#min_num").val()
        },
        success: function(response){
            document.write(response);
        }
    })
}

   
// function searchajax(){
//     $("#searchword").keyup(function(){
//         var words = $("#searchword").val();
//         if( words != ''){
//             $.ajax({
//                 type: 'POST',
//                 url: '/browser/searchData/',
//                 data: { searchwords : words},
//                 dataType: 'json',
//                 success: function(result){
//                     if ( result.length > 0){
//                         var str = ''
//                         for (var i=0; i<result.length; i++){
//                             str += '<span>'+ result[i].data + '</span><br/>';
//                         }
//                         $("#results").html(str);
//                     } else{ $("#results").html(""); }
//                 },
//                 error: function(e) {console.log('error:' + e.status);}
//             });
//         } else{ $("#results").html(""); }
//     });
// }
