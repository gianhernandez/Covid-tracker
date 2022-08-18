
// Pagination library
$(document).ready( function () {
    $('#country-table').DataTable();
} );


// Death Gif
$(document).ready(function()
{
    $("#death").hover(
        function()
        {
            $(this).attr("src", "/static/images/death.gif");
        },
        function()
        {
            $(this).attr("src", "/static/images/death-static.jpeg");
        }
    );
});

$(document).ready(function()
{
    $("#covid").hover(
        function()
        {
            $(this).attr("src", "/static/images/coronavirus.gif");
        },
        function()
        {
            $(this).attr("src", "/static/images/coronavirus-static.png");
        }
    );
});




$(document).ready(function()
{
    $("#heart").hover(
        function()
        {
            $(this).attr("src", "/static/images/heart.gif");
        },
        function()
        {
            $(this).attr("src", "/static/images/heart-static.png");
        }
    );
});