'use strict'

// Why not do it in JSON?
/*
  Each top level

*/

function treeToLuna(t) {
  console.log(t)
  var k = Object.keys(t)
  var resultString = ''
  var resultEndCharacters = []

  for (let i=0; i<k.length; i++) {
      console.log(resultString)
      if (typeof t[ k[i] ] == 'object') {
        resultString += k[i] + '('
        resultEndCharacters.push(')')
        resultString += treeToLuna(t[ k[i] ])
      } else {
        if (k[i] == 'IMG') {
          resultString += k[i] + '({})'
        } else {
          resultString += k[i] + '()'
        }

        // Sibling?
        if (i < k.length - 1) {
          resultString += ', '
        }
      }
  }

  // Add end characters
  for (let i=resultEndCharacters.length-1; i >= 0; i--) {
    resultString += resultEndCharacters[i]
  }

  return resultString

}
// DIV([P([IMG({})]), B([])])
var test = {
  DIV: {
    P: {
      IMG: true,
      B: true
    }
  }
}

console.log(treeToLuna(test))

function htmlToLuna(html) {
    var htmlParts = html.match(/<\/?[a-zA-Z \/]+>/g)
    var htmlStack = []
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



// console.log(htmlToLuna("<div><img /></div>"))
// Expected output: DIV([IMG({})]
// console.log(htmlToLuna("<div><p><img /></p><b></b></div>"))
// Expected: DIV([P([IMG({})]), B([])])
