// function myFunction() {
//     var txt;
//     if (confirm("Wanna Delete This Parcel?")){
//         window.location.href = '{% url "home" %}'
//     }
//
// }


function loadCon() {
    var xhttp = new XMLHttpRequest(ox);
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("loadDIV").innerHTML = this.responseText;
        }
    };
    xhttp.open('GET', 'order-details/ox', true);
    xhttp.send();
}


$('.accordian-body').on('show.bs.collapse',
    function () {
        $(this).closest("table")
            .find(".collapse.in")
            .not(this)
            .collapse('toggle')
})