'use strict'

function Node(data) {
  this.data = data
  this.parent = null
  this.children = []
}

function Tree(rootData) {
  var rootData = new Node(rootData)
  this._root = rootData
}

function DFS_Luna(n) {
  var resultString = ''

  for (var i=0; i<n.children.length; i++) {
    var thisChild = n.children[i]
    if (thisChild.data == 'IMG') {
      resultString += 'IMG({'
      resultString += DFS_Luna(thisChild)
      resultString += '})'
    } else {
      resultString += thisChild.data + '(['
      resultString += DFS_Luna(thisChild)
      resultString += '])'
    }

    if (i < n.children.length - 1) {
      resultString += "\, "
    }
  }

  return resultString

}

function htmlToLuna(html) {
    var htmlParts = html.match(/<\/?[a-zA-Z \/]+>/g)
    var htmlTree = new Tree(null)
    var currentNode = htmlTree._root

    if (htmlParts == null) {
      return ''
    }

    for (var i=0; i<htmlParts.length; i++) {
      var thisPart = htmlParts[i]
      // Remove the carrots...
      var stringToPush = thisPart.substr(1, thisPart.length-2).toUpperCase()

      if (stringToPush[0] == '/') {
        // End
        currentNode = currentNode.parent

      } else if (stringToPush[stringToPush.length-1] == '/') {
        var thisNode = new Node(stringToPush.substr(0, stringToPush.length-2))
        thisNode.parent = currentNode
        currentNode.children.push(thisNode)

      } else {
        var thisNode = new Node(stringToPush)
        thisNode.parent = currentNode
        currentNode.children.push(thisNode)
        currentNode = thisNode

      }
    }

    return DFS_Luna(htmlTree._root)
}
