// [lowest y coord, highest y coord]
function yRange(mouseCoordinates) {
    if (mouseCoordinates[0][1] < mouseCoordinates[1][1]) {
        return [mouseCoordinates[0][1],
                mouseCoordinates[1][1]]
    } else {
        return [mouseCoordinates[1][1],
                mouseCoordinates[0][1]]
    }
}

function taskInRange(dimensions, indexNumber, yRange) {
    console.log('task num:', indexNumber)
    var taskTop = dimensions[1] * indexNumber + (dimensions[2] * indexNumber)
    console.log('task top:', taskTop)

    var taskBottom = taskTop + dimensions[1]
    console.log('taskl bottom:',  taskBottom)

    if (yRange[0] <= taskTop  && taskTop <= yRange[1]) {
      console.log(yRange[0], taskTop, yRange[1], yRange[0] <= taskTop <= yRange[1])
      console.log('top')
        return true
    } else if (yRange[0] <= taskBottom && taskBottom <= yRange[1]) {
      console.log('bottom')
        return true
    } else {
      console.log('false')
        return false
    }
}

function multiSelection(dimensions, tasks, mouseCoordinates) {
 // I think I only have to judge the height. No matter the case, any horizontal line will at most touch one element. By judging the y range, I can determine if any member of the array is within the selection

    var resultArray = []
    console.log('coords:', mouseCoordinates)
    var yR = yRange(mouseCoordinates)
    console.log('yrange:', yR)

    tasks.forEach(function(task, index) {
        if (taskInRange(dimensions, index, yR) == true)
        {
            resultArray.push(task)
        }
    })

    return resultArray

}


var the_dimensions = [135, 9, 1]
var the_tasks = ["Task 1",
 "Task 2",
 "Task 3",
 "Very Important Task",
 "Not So Important Task",
 "Yet Another Task",
 "The last task"]
var the_mouseCoordinates = [[132,42],
 [35,13]]

console.log(multiSelection(the_dimensions, the_tasks, the_mouseCoordinates))
