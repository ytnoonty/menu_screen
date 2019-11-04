class Animation {
  constructor () {}

  getMovement(liTicker) {
    let liTotalWidth = 0;
    let tickerWidth = 0;
    let totalDivTicker = 0;
    let totalLiWidth = 0;
    liTicker.forEach(function(tick){
      let elWidth = getElementWidth(tick);
      let beforePseudoWidth = getPseudoElementWidth(tick, "before", "width");
      let afterPseudoWidth = getPseudoElementWidth(tick, "after", "width");
      totalLiWidth += beforePseudoWidth + afterPseudoWidth + elWidth;
    });
    let widthMovement = "translateX(-" + totalLiWidth + "px)";
  return widthMovement;
  }
  getElementWidth(el) {
    // console.log("***********************************************");
    // console.log("ABOUT TO ANIMATE THE TICKER!");
    // console.log(el.innerText);
    let elInnerWidth = el.offsetWidth;
    // console.log(elInnerWidth);
    let elWidthStyle = getComputedStyle(el);
    // console.log(elWidthStyle);
    let elMarginLeftWidth = parseInt(elWidthStyle.marginLeft);
    // console.log(elMarginLeftWidth);
    let elMarginRightWidth = parseInt(elWidthStyle.marginRight);
    // console.log(elMarginRightWidth);
    let elTotalWidth = 0;
    elTotalWidth += elInnerWidth;
    elTotalWidth += elMarginLeftWidth;
    elTotalWidth += elMarginRightWidth;
    // console.log(elTotalWidth);
    // console.log("***********************************************");
    return elTotalWidth;
  }
  runThisTest() {
    console.log("RUNNING THIS TEST");
  }
  getThis() {
    this.runThisTest();
  }


  getPseudoElementWidth(el, position, property) {
    let totalElWidth = 0;
    position = ":" + position;
    var elWidth = window.getComputedStyle(
      el, position
    ).getPropertyValue(property);

    elWidth = parseInt(elWidth.slice(0,2));
    if (isNaN(elWidth)) {
      elWidth = 0;
    } else {
    }

    totalElWidth = elWidth;
    // console.log("position: " + position + " " + totalElWidth);
    return totalElWidth;
  }

  animateTicker(el, movement, duration) {
    el.animate([
      { transform: 'translateX(100vw)'},
      { transform: movement}
    ], {
      duration: duration,
      iterations: Infinity
    });
  }

}
