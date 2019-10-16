let flashMsgDiv = document.getElementById('flash-msg-div');
let updateProcessPrint = document.getElementById('update-tv-screen');
console.log('in the javascript');

// let updateBeerList = document.getElementById('edit-beerlist');
// // updateBeerList.addEventListener('submit', loadBeerList);
// updateBeerList.onsubmit = function(){loadBeerList};


if (updateProcessPrint != null) {
  updateProcessPrint.addEventListener('click', function(e){
    window.location.reload();
    screenRefresh();
    loadBeerlist();
    // loadTicker();
  });
}

// // loadTicker();
// moveTheStuff();

loadBeerlist();
// // screenRefresh();


// function moveNode() {
//   let newli = liTicker[0].cloneNode(true);
//   liTicker[0].parentNode.removeChild(liTicker[0]);
//   let ul = document.querySelector(".list-bts-coming-soon");
//   ul.appendChild(newli);
//   // ul.lastElementChild.removeAttribute("style");
//   ul.lastElementChild.style.marginLeft = "0px";
// }
//
// moveTicker();
// function moveTicker() {
//   let pos = 0;
//   let id = setInterval(frame, 10);
//
//   tickerWidth = 0;
//
//   function frame() {
//     // if (pos < -(liTicker[0].offsetWidth)) {
//     if (pos < -(liTotalWidth)) {
//       pos = 0;
//
//       moveNode();
//
//       liTicker = document.querySelectorAll(".info");
//
//       let liInnerWidth = liTicker[0].offsetWidth;
//       let widthStyle = getComputedStyle(liTicker[0]);
//       let marginLeftWidth = parseInt(widthStyle.marginLeft);
//       let marginRightWidth = parseInt(widthStyle.marginRight);
//
//       console.log("liInnerWidth = " + liInnerWidth);
//       console.log("marginLeftWidth = " + marginLeftWidth);
//       console.log("marginRightWidth = " + marginRightWidth);
//       liTotalWidth = 0;
//       liTotalWidth += liInnerWidth;
//       liTotalWidth += marginLeftWidth;
//       liTotalWidth += marginRightWidth;
//       console.log("pos = " + pos);
//       console.log("liTotalWidth = " + liTotalWidth);
//       console.log(" ");
//
//       // clearInterval(id);
//       // pos = 0;
//     } else {
//       pos--;
//       // console.log("pos = " + pos);
//       // divTicker.style.top = '0' + 'px';
//       // divTicker.style.left = pos + 'px';
//       liTicker[0].style.marginLeft = pos + 'px';
//     }
//   }
// }

// ////////////////////////////////////////////////////
// // START loadTicker()
// ///////////////////////////////////////////////////
function loadTicker(e) {
  // console.log('testing function works');
  const xhr = new XMLHttpRequest();
  // console.log('READYSTATE1', xhr.readyState);
  //Open
  // xhr.open('POST', '/update', true);
  xhr.open('POST', '/update', true);
  // console.log('READYSTATE2', xhr.readyState);
  // console.log('STATUS before onload', this.status);
  // xhr.onload
  xhr.onload = function(){
    // console.log('READYSTATE3', xhr.readyState);
    // console.log('STATUS after onload', this.status);
    if (this.status === 200) {
      // console.log(this.responseText);

      let data = JSON.parse(this.responseText);
      let data1721 = data.slice(16,21);
      let tickerhtml = '';

      let beer1 = document.querySelector(".info1");
      tickerhtml = `${data1721[0].name}`;
      if (beer1 != null) {
        beer1.innerHTML = tickerhtml;
        let width = beer1.offsetWidth;
        // console.log("info1 width: " + width);
      }
      let beer2 = document.querySelector(".info2");
      tickerhtml = `${data1721[1].name}`;
      if (beer2 != null) {
        beer2.innerHTML = tickerhtml;
        let width = beer2.offsetWidth;
        // console.log("info2 width: " + width);
      }
      let beer3 = document.querySelector(".info3");
      tickerhtml = `${data1721[2].name}`;
      if (beer3 != null) {
        beer3.innerHTML = tickerhtml;
        let width = beer3.offsetWidth;
        // console.log("info3 width: " + width);
      }
      let beer4 = document.querySelector(".info4");
      tickerhtml = `${data1721[3].name}`;
      if (beer4 != null) {
        beer4.innerHTML = tickerhtml;
        let width = beer4.offsetWidth;
        // console.log("info4 width: " + width);
      }
      let beer5 = document.querySelector(".info5");
      tickerhtml = `${data1721[4].name}`;
      if (beer5 != null) {
        beer5.innerHTML = tickerhtml;
        let width = beer5.offsetWidth;
        // console.log("info5 width: " + width);
      }
    }
  }
  xhr.send();
  setTimeout(loadTicker,250);
  e.preventDefault();
}
// ////////////////////////////////////////////////////
// // END loadTicker()
// ///////////////////////////////////////////////////


//////////////////////////////////////////////////////
// START screenRefresh()
/////////////////////////////////////////////////////
function screenRefresh(){
  let currentTime = new Date();
  let hour = currentTime.getHours();
  let min = currentTime.getMinutes();
  let sec = currentTime.getSeconds();
  let millSec = currentTime.getMilliseconds();
  // console.log('hour is: ' + hour);
  // console.log('min is: ' + min);
  // console.log('sec is: ' + sec);
  // console.log('millSec is: ' + millSec);
  // if ((hour == 6 || hour == 10 || hour == 14 || hour == 16 || hour == 18 || hour == 20 || hour == 22 || hour == 24) && min == 1 && sec == 1 && millSec < 250){
  // if (min == 1 && (sec == 1 || sec == 31) && millSec < 250){
  if (min == 1 && sec == 1 && millSec < 250){
  // if ((sec == 1 || sec == 31) && millSec < 250){
    window.location.reload();
    // console.log('in the new function and minutes is: ' + min);
    // console.log('sec is: ' + sec);
    // console.log('millSec is: ' + millSec);
    // console.log('************************SCREEN UPDATED*******************');
  }
}
//////////////////////////////////////////////////////
// END screenRefresh()
/////////////////////////////////////////////////////

//////////////////////////////////////////////////////
// START loadBeerlist()
/////////////////////////////////////////////////////
function loadBeerlist(e) {
  console.log('testing function works');

  const xhr = new XMLHttpRequest();
  // console.log('READYSTATE1', xhr.readyState);

  //Open
  xhr.open('POST', '/update', true);
  // console.log('READYSTATE2', xhr.readyState);

  // console.log('STATUS before onload', this.status);
  // xhr.onload
  xhr.onload = function(){
    // console.log('READYSTATE3', xhr.readyState);
    // console.log('STATUS after onload', this.status);
    if (this.status === 200) {
      // console.log(this.responseText);
      // let ul = document.createElement('ul');
      //use this as a reference
      // ul.setAttribute("id", "this-is-the-id");
      // ul.classList.add = 'list-group-flush';
      let data = JSON.parse(this.responseText);
      let data0116 = data.slice(0,16);
      let data1721 = data.slice(16,21);
      let data0108 = data.slice(0,8);
      let data0816 = data.slice(8,16);

////////////////////////////////////////////////////////////
// START BEERS_PRINT.HTML UPDATE
////////////////////////////////////////////////////////////
      let beerListDivBP = document.getElementsByClassName('beer-list-div-bp');
      // beerListDivBP[0].innerHTML = "";
      // console.log(beerListDiv);
      let htmlStuffBP = '';

      htmlStuffBP += `<ul id="" class='list-group-flush'>`;
      data0116.forEach(function(beer){
        htmlStuffBP += `<li id="" class='list-group-item'>${beer.id}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - ${beer.style} - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
      });
      htmlStuffBP += `</ul>`;
      if (beerListDivBP[0] !== undefined) {
        beerListDivBP[0].innerHTML = htmlStuffBP;
      }

      let monthPBP = document.getElementsByClassName('month-p-bp');
      if (monthPBP[0] !== undefined) {
        monthPBP[0].innerHTML = `<span class="mx-3 larger-text txt-clr-grn">${data1721[0].name}</span>`;
      }

      let comingsoonPBP = document.getElementById('comingsoon-p-bp');
      if (comingsoonPBP !== null) {
        comingsoonPBP.innerHTML = `
        <span class="mx-4 larger-text txt-clr-grn">${data1721[1].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[2].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[3].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[4].name}</span>
        `;
      }
////////////////////////////////////////////////////////////
// END BEERS_PRINT.HTML UPDATE
// /////////////////////////////////////////////


/////////////////////////////////////////////////////////////
// START PROCCESS_PRINT.HTML UPDATE
/////////////////////////////////////////////////////////////
      let beerListDivPP = document.getElementsByClassName('beer-list-div-pp');
      // beerListDivPP[0].innerHTML = "";
      // console.log(beerListDivPP[0]);
      let htmlStuffPP = '';

      htmlStuffPP += `<ul id="" class='beer-list-loop-pp list-group-flush'>`;
      data0116.forEach(function(beer){
        htmlStuffPP += `<li id="" class='list-group-item-pp list-group-item'>${beer.id}.  <span class="larger-text txt-clr-grn">${beer.name}</span> - <span class="bold-font italic-font">${beer.style}</span> - ${beer.abv}% ABV - ${beer.ibu} IBU - ${beer.location} - <span class="italic-font">${beer.brewery}</span></li>`;
      });
      htmlStuffPP += `</ul>`;
      if (beerListDivPP[0] !== undefined) {
        beerListDivPP[0].innerHTML = htmlStuffPP;
      }

      let monthPPP = document.getElementsByClassName('month-p-pp');
      if (monthPPP[0] !== undefined) {
        monthPPP[0].innerHTML = `<span class="mx-3 larger-text txt-clr-grn">${data1721[0].name}</span> - <span class="bold-font italic-font">${data1721[0].style}</span>`;
      }

      let comingsoonPPP = document.getElementById('comingsoon-p-pp');
      console.log(comingsoonPPP);
      if (comingsoonPPP !== null) {
        comingsoonPPP.innerHTML = `
        <span class="mx-4 larger-text txt-clr-grn">${data1721[1].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[2].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[3].name}</span>
        <span class="mx-4 larger-text txt-clr-grn">${data1721[4].name}</span>
        `;
        // comingsoonPPP.innerHTML = "";
      }

/////////////////////////////////////////////////////////////
// END PROCCESS_PRINT.HTML UPDATE
////////////////////////////////////////////////



// /////////////////////////////////////////////


/////////////////////////////////////
// example6
/////////////////////////////////////
let example6 = document.getElementById('example6');
let example6HTML = '';
example6HTML = `
<div class="row">
  <div class="col-lg">
    <div class="list-group">
      <ul class="list-group-flush list-group-bts">`;
      //USED FOR TESTING THE ajax update
      //uncomment line below and reload browser or reboot pi
      // example6HTML += `<div></div>`;
        data0108.forEach(function(beer){
          example6HTML += `
          <li class="cardvs">
            <table>
              <tr>
                <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
              </tr>
              <tr class="left-spacer beer-screen-tr">
                <td class="bold-font w-third">${beer.style}</td>
                <td class="w-forth">ABV ${beer.abv}%</td>
                <td class="italic-font bold-font w-third">${beer.brewery}</td>
              </tr>
            </table>
          </li>`
        });
example6HTML += `
      </ul>
    </div>
  </div>
  <div class="col-lg">
    <div class="list-group">
      <ul class="list-group-flush list-group-bts">`;
        data0816.forEach(function(beer){
          example6HTML += `
          <li class="cardvs">
            <table>
              <tr>
                <h1 class="italic-font bold-font txt-clr-ylw left-spacer no-btm-margin"><span class="">${beer.name}</span></h1>
              </tr>
              <tr class="left-spacer beer-screen-tr">
                <td class="bold-font w-third">${beer.style}</td>
                <td class="w-forth">ABV ${beer.abv}%</td>
                <td class="italic-font bold-font w-third">${beer.brewery}</td>
              </tr>
            </table>
          </li>`
        });
example6HTML += `
      </ul>
    </div>
  </div>
</div>`;
if (example6 !== null) {
  // console.log(example6HTML);
  example6.innerHTML = example6HTML;
}
/////////////////////////////////////
// END example6
/////////////////////////////////////

/////////////////////////////////////////////
/////////////////////////////////////////////

    }
  }

  xhr.send();
  // moveTheStuff();
  console.log('BEFORE REFRESH');
  // setTimeout(screenRefresh(),5000);
  screenRefresh();
  console.log('AFTER REFRESH')
  // loadTicker();
  setTimeout(function(){
    flashMsgDiv.style.display = 'none';
  },2500);

  setTimeout(loadBeerlist,10000);

  e.preventDefault();
  // return true;
}

//////////////////////////////////////////////////////
// END loadBeerlist()
/////////////////////////////////////////////////////
