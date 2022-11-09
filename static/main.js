function choose_exercise() {
            
    let which_exercise = document.getElementById('exercise');
    if (which_exercise.value == "상체 루틴") {
        $.ajax({
            type: "GET",
            url: "/push_up",
            data: {},
            success: function(response){
                document.write(response); 
            }
        });
        alert("상체 루틴 ㄱㄱㄱ");
    }
    else if (which_exercise.value == "전신 루틴") {
        $.ajax({
            type: "GET",
            url: "/burpee",
            data: {},
            success: function(response){
                
            }
        });
        alert("전신 루틴 ㄱㄱㄱ");
    }
    else if (which_exercise.value == "하체 루틴") {
        $.ajax({
            type: "GET",
            url: "/deck_of_pain_rep",
            data: {},
            success: function(response){
                console.log(response)
            }
        });
        alert("하체 루틴 ㄱㄱㄱ");
    }
    else
        alert("운동종류를 입력해주십시오!")
}


// $.ajax({
//     type: "GET",
//     url: "/test?which_exercise=봄날은간다",
//     data: { 
//         exercise: which_exercise()
//     },
//     dataType: "json",
//     success: function(response){
//     console.log(response)
//     }
// });

// $.ajax({
//     type: "POST",
//     url: "/test",
//     data: { 
//         exercise: which_exercise()
//     },
//     dataType: "json",
//     success: function(response){
//     console.log(response)
//     }
// });


