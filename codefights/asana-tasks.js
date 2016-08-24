function max(a, b) {
  return a > b ? a : b
}

function DP_BuildTable(workingHours, tasks) {
  // Build a table of tasks and working amounts
  var taskTable = new Array(tasks.length)
  for (var i=0; i<taskTable.length; i++) {
      taskTable[i] = new Array(workingHours + 1)

      // i = tasks index, j = working hours
      for (var j=0; j<(workingHours + 1); j++) {
        if (i == 0) {
            // First row
            taskTable[i][j] = tasks[i] > j ? 0 : tasks[i]
        } else {
            var taskValue = tasks[i]
            if (taskValue > j) {
                taskTable[i][j] = max(0, taskTable[i-1][j])
            } else {
                var taskAddedIndex = j - taskValue
                var taskAddedValue
                    = taskValue + taskTable[i-1][taskAddedIndex]

                taskTable[i][j] = max(taskAddedValue, taskTable[i-1][j])
            }

        }
      }
  }
    // console.log(taskTable)
    return taskTable
}

function DP_ReturnSolution(table, tasks) {
    var rows = table.length
    var columns = rows > 0 ? table[0].length : 0
    var resultIndicies = []



    var i = rows-1, j = columns-1
    while(i >= 0 && j >= 0) {
        if (i == 0) {
            if (table[i][j] != 0) {
              resultIndicies.push(0)
            }
            break
        } else if (table[i][j] == table[i-1][j]) {
            i -= 1
        } else {
            resultIndicies.push(i)
            j -= tasks[i]
            i -= 1
        }
    }

    // console.log('sol:', resultIndicies)
    return resultIndicies

}

function tasksScheduling(workingHours, tasks) {
  for (var i=0; i<tasks.length; i++) {
        if (tasks[i] > workingHours) {
            return -1
        }
    }

  var tasksAvailable = tasks
  var days = 0

  // console.log('hours', workingHours)

  // Build the table
  while (tasksAvailable.length > 0) {
      // console.log('tasks', tasksAvailable)
      var taskTable = DP_BuildTable(workingHours, tasksAvailable)
      var taskIndicies = DP_ReturnSolution(taskTable, tasksAvailable)
      console.log('indicies', taskIndicies)
      for (var i=0; i<taskIndicies.length; i++) {
          tasksAvailable.splice(taskIndicies[i], 1)
      }

      days += 1
  }

  return days
}

// workingHours: 13
// tasks: [2, 3, 3, 3, 3, 5, 7]
// tasksScheduling(13, [2, 3, 3, 3, 3, 5, 7])
// workingHours: 2
// tasks: [1, 2, 2, 1, 1, 2, 1, 1]
// console.log('final sol:', tasksScheduling(2, [1, 2, 2, 1, 1, 2, 1, 1]))


/* Thinking through a dynamic programming solution
 * 0-1 knapsack...

 * What is the max weight we can fit in the knapsack?
 * Take those elements out of the knapsack, repeat until zero are left
 *        0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13
 *      +----------------------------------------------------------
 *   2  |-1 |-1 | 2 |_2 | 2 | 2 | 2 | 2 | 2 | 2 | 2  | 2  | 2  | 2
 *   3  |-1 |-1 | 2 | 3 | 3 |_5 | 5 | 5 | 5 | 5 | 5  | 5  | 5  | 5
 *   3  |-1 |-1 | 2 | 3 | 3 | 5 | 6 | 6 |_8 | 8 | 8  | 8  | 8  | 8
 *   3  |-1 |-1 | 2 | 3 | 3 | 5 | 6 | 6 | 8 | 9 | 9  | 11 | 11 | 11
 *   3  |-1 |-1 | 2 | 3 | 3 | 5 | 6 | 6 | 8 | 9 | 9  | 11 | 12 | 12
 *   5  |-1 |-1 | 2 | 3 | 3 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |_13
 *   7  |-1 |-1 | 2 | 3 | 3 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13
 *
 *        0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13
 *   3   -1 |-1 |-1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3  | 3  | 3  | 3
 *   3   -1 |-1 | -1
 *   7
 *
 *     0 | 1 | 2
 *  1 -1 | 1 | 1
 *  2 -1 | -1|_2
 *  1 -1 | 1 | 2
 * */
