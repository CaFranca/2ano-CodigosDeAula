
var A = 10;
var B = 5;
var C = 8;


if (A <= B && A <= C) {
    if (B <= C) {
        console.log(A, B, C); // A, B, C
    } else {
        console.log(A, C, B); // A, C, B
    }
} else if (B <= A && B <= C) {
    if (A <= C) {
        console.log(B, A, C); // B, A, C
    } else {
        console.log(B, C, A); // B, C, A
    }
} else {
    if (A <= B) {
        console.log(C, A, B); // C, A, B
    } else {
        console.log(C, B, A); // C, B, A
    }
}
