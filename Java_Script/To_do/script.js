let count = 1
let obj = {}
while (true) {
    let userInput = prompt("  Bolimni tanlang:\n 1.add, 2.list, 3.delete, 4.exit")
    if(userInput == 1 || userInput == "add"){
        let userInput2 = prompt("vazifa kiriting")
        obj[count] = userInput2
        count++
        console.log(obj);
    }
    else if(userInput == 2 || userInput == "list"){
        let myStr = ''
        for(let i in obj){
            console.log(i, obj[i]);
            myStr += `${i}. ${obj[i]} \n`
        }
        alert(myStr)
    }
    else if(userInput == 3 || userInput == "delete"){
        let myStr = ''
        for(let i in obj){
            console.log(i, obj[i]);
            myStr += `${i}. ${obj[i]} \n`
        }
        let userInputDelete = prompt(`raqamni tanlang:\n ${myStr}`)

        delete obj[userInputDelete]
    }

    else if(userInput == 4 || userInput == "exit"){
        break
    }
}
