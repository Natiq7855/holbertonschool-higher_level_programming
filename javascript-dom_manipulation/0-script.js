#!/usr/bin/node

const header = document.querySelector("h1");

if (header){
    header.style.color = #FF0000;
} else{
    console.warn("no header element");
}