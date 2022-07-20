function gradingStudents(grades) {
    for (let i = 0; i < grades.length; i++) {
        const nextMultiple = Math.ceil(grades[i] / 5) * 5;
        if (nextMultiple - grades[i] < 3 && grades[i] >= 38) {
            grades[i] = nextMultiple;
        }
    }
    return grades;
}

console.log(gradingStudents([73, 67, 38, 33]));