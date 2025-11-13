// 🎮 Quick Quiz Game Logic

const questions = [
    { text: "Has Bitcoin gone up in the last 24 hours?", answer: "down" },
    { text: "Has the average global temperature increased this week?", answer: "up" },
    { text: "Is the current Ethereum trend rising?", answer: "up" },
    { text: "Has the USD to EUR exchange rate fallen?", answer: "down" },
    { text: "Is tech stock index (NASDAQ) trending upward?", answer: "up" },
    { text: "Is rainfall in Jerusalem higher today than yesterday?", answer: "down" },
    { text: "Has gold’s value increased this week?", answer: "up" },
    { text: "Is the average Bitcoin trading volume going down?", answer: "down" },
    { text: "Has global energy demand increased this month?", answer: "up" },
    { text: "Is the current global inflation trend rising?", answer: "up" }
];

let current = 0;
let score = 0;

const questionEl = document.getElementById("question");
const feedbackEl = document.getElementById("feedback");
const scoreEl = document.getElementById("score");
const nextBtn = document.getElementById("next-btn");

const upBtn = document.getElementById("btn-up");
const downBtn = document.getElementById("btn-down");

function showQuestion() {
    const q = questions[current];
    questionEl.textContent = q.text;
    feedbackEl.textContent = "";
    nextBtn.classList.add("hidden");
}

function checkAnswer(choice) {
    const correct = questions[current].answer;
    if (choice === correct) {
        score++;
        feedbackEl.textContent = "✅ Correct!";
        feedbackEl.style.color = "#10B981";
    } else {
        feedbackEl.textContent = `❌ Wrong! Correct answer: ${correct.toUpperCase()}`;
        feedbackEl.style.color = "#EF4444";
    }

    scoreEl.textContent = `Score: ${score} / 10`;
    nextBtn.classList.remove("hidden");
}

upBtn.addEventListener("click", () => checkAnswer("up"));
downBtn.addEventListener("click", () => checkAnswer("down"));

nextBtn.addEventListener("click", () => {
    current++;
    if (current < questions.length) {
        showQuestion();
    } else {
        questionEl.textContent = "🏁 Quiz Complete!";
        feedbackEl.textContent = `Your final score: ${score} / 10`;
        nextBtn.classList.add("hidden");
        upBtn.style.display = "none";
        downBtn.style.display = "none";
    }
});

showQuestion();
