function arrayToLuna(arr) {
  var resultString = ''
  var resultStringClosers = []

  for (let i=0; i<arr.length; i++) {
    let thisItem = arr[i]
    let thisItemKeys = Object.keys(thisItem)

    console.log(thisItemKeys)

    if (i > 0) {
      resultString += ', '
    }

    for (let j=0; j<thisItemKeys.length; j++) {
      let thisKey = thisItemKeys[j]



      if (thisKey == 'IMG') {
        resultString += thisKey + '({})'
      } else {
        resultString += thisKey + '(['
        resultStringClosers.push('])')
      }

      if (typeof thisItem[thisKey] == 'object') {
        resultString += arrayToLuna(thisItem[thisKey])
      }

    }

    for (let j=0; j<thisItemKeys.length; j++) {
      resultString += resultStringClosers.pop() || ''
    }
  }



  return resultString

}

// DIV([P([IMG({})]), B([])])
var test = [{'DIV': [
  {P: [
    {IMG: true}
  ]},
  {B: true}
]}]

console.log(arrayToLuna(test))

function htmlToLuna(html) {
    var htmlParts = html.match(/<\/?[a-zA-Z \/]+>/g)
    var resultString = ''

    for (index in htmlParts) {
        // Remove the carrots...
      var stringToPush = htmlParts[index].substr(1, htmlParts[index].length-2).toUpperCase()
      if (stringToPush[0] == '/') {
        // End tag...
        resultString += ')'
      } else if (stringToPush[stringToPush.length-1] == '/') {
        // Solo tag
        resultString += '[' +
          stringToPush.substr(0, stringToPush.length-2) + '{}'
          + ']'
      } else {
        resultString += stringToPush + '('
      }


    }

    return resultString


}

// console.log(htmlToLuna('<div><img /></div>'))
