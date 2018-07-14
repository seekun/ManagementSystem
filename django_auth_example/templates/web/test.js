var dark = "background-color= black";
var day = "background-color= white";

var button = document.querySelect(".nav");
var web = document.querySelect("body");

function LightSwitch() {
    if (web.style.cssText == dark) {
        web.style.cssText = day;
        alert("Day mode");
    } else {
        web.style.cssText = dark;
        alert("Night mode");
    }
}
button.onclick = lightSwitch