let count = 1;
let obj = {};

while (true) {
    let userInput = prompt(
        "     Telefon malumotnomasi \n              Bo'limni tanlang:\n\n 1. Yangi kontakt qo'shish \n 2. Kontaktni qidirish \n 3. Kontaktni o'chirish \n 4. Barcha kontaktlarni ko'rsatish \n 5. Mavjud komandalarni ko'rsatish \n 6. Dasturdan chiqish"
    );

    if (userInput == 1) {
        let userInput2 = prompt("Ism va telefon nomerni kiriting (masalan: Ism, +998991234567)");
        let [name, phone] = userInput2.split(',');

        if (name && phone) {
            obj[count] = {
                name: name.trim(),
                phone: phone.trim()
            };
            count++;
            console.log(obj);
        } else {
            alert("Ism va telefon raqamini to'g'ri kiriting.");
        }
    } else if (userInput == 2) {
        let searchPhone = prompt("Qidiriladigan telefon raqamini kiriting (masalan: +998991234567)");

        let foundUser = null;

        for (let i in obj) {
            if (obj[i].phone === searchPhone.trim()) {
                foundUser = obj[i];
                break;
            }
        }

        if (foundUser) {
            alert(`Foydalanuvchi topildi: Ism - ${foundUser.name}, Telefon - ${foundUser.phone}`);
        } else {
            alert("Foydalanuvchi topilmadi.");
        }
    } else if (userInput == 3) {
        let myStr = '';
        for (let i in obj) {
            myStr += `${i}. ${obj[i].name}, ${obj[i].phone}\n`;
        }
        let userInputDelete = prompt(`Ochiriladigan kontakt raqamini tanlang:\n ${myStr}`);

        if (obj[userInputDelete]) {
            delete obj[userInputDelete];
            alert("Kontakt muvaffaqiyatli o'chirildi.");
        } else {
            alert("Bunday kontakt mavjud emas.");
        }
    } else if (userInput == 4) {
        let myStr = '';

        for (let i in obj) {
            myStr += `${i}. ${obj[i].name}, ${obj[i].phone}\n`;
        }

        alert(myStr);
    } else if (userInput == 5) {
        alert(
            "Bo'limni tanlang:\n\n 1. Yangi kontakt qo'shish \n 2. Kontaktni qidirish \n 3. Kontaktni o'chirish \n 4. Barcha kontaktlarni ko'rsatish \n 5. Mavjud komandalarni ko'rsatish \n 6. Dasturdan chiqish"
        );
    } else if (userInput == 6 || userInput.toLowerCase() == "exit") {
        break;
    } else {
        alert("Noto'g'ri buyruq kiritildi, iltimos, qayta urinib ko'ring.");
    }
}
