async function askAI() {

    const notes = document.getElementById("notes").value;
    const question = document.getElementById("question").value;

    const answerBox = document.getElementById("answer");

    if (!notes || !question) {
        answerBox.innerText = "Please enter both notes and a question.";
        return;
    }

    answerBox.innerText = "🤔 Thinking...";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question,
                    notes: notes
                })
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong");
        }

        answerBox.innerText = data.answer;

    } catch (error) {

        answerBox.innerText =
            "❌ Error: " + error.message;

    }
}