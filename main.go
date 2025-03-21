package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"math/rand"
	"time"

	"github.com/glebarez/sqlite"
	"gorm.io/gorm"
)

// Question struct for database mapping
type Question struct {
	ID       uint   `gorm:"primaryKey"`
	Question string `gorm:"not null"`
	Answer   bool   `gorm:"not null"`
}

// Function to initialize database
func InitDB() (*gorm.DB, error) {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		return nil, err
	}
	return db, nil
}

// Function to fetch random questions ensuring no repetitions
func GetUniqueRandomQuestions(db *gorm.DB, limit int) ([]Question, error) {
	var allQuestions []Question
	result := db.Find(&allQuestions)
	if result.Error != nil {
		return nil, result.Error
	}

	if len(allQuestions) < limit {
		return allQuestions, nil // If fewer questions exist, return all available
	}

	rand.Seed(time.Now().UnixNano())

	uniqueQuestions := make([]Question, 0, limit)
	usedIndexes := make(map[int]bool)

	for len(uniqueQuestions) < limit {
		index := rand.Intn(len(allQuestions))
		if !usedIndexes[index] {
			uniqueQuestions = append(uniqueQuestions, allQuestions[index])
			usedIndexes[index] = true
		}
	}

	return uniqueQuestions, nil
}

func main() {
	fmt.Println("Welcome to my quiz game!")

	myname := "Nachiket"
	fmt.Printf("Hi, I am %v\n", myname)

	var name string
	fmt.Println("What is your name?")
	fmt.Scanln(&name)
	fmt.Printf("Hi %v!\n", name)

	var play string
	fmt.Printf("%v, do you want to play my quiz game? (yes/no): ", name)
	fmt.Scanln(&play)

	play = strings.ToLower(strings.TrimSpace(play))

	if play != "yes" && play != "y" {
		fmt.Println("Nevermind, fuck you bitch!!")
		return
	}

	fmt.Println("Yay! Let's play.")

	var age uint
	fmt.Println("Enter your age:")
	fmt.Scan(&age)

	if age < 18 {
		fmt.Printf("You're too young, kiddo! This game contains some serious stuff. Come back after %v year(s).\n", 18-age)
		return
	}

	fmt.Println("Alright, alright, alright. Be ready for some serious stuff coming your way.")
	fmt.Println("These questions will be true or false. Input 't' for True and 'f' for False.")

	// Clear input buffer before taking quiz inputs
	reader := bufio.NewReader(os.Stdin)
	_, _ = reader.ReadString('\n') // Consume the leftover newline

	// Connect to database
	db, err := InitDB()
	if err != nil {
		fmt.Println("Failed to connect to database:", err)
		return
	}

	// Fetch random unique 10 questions
	questions, err := GetUniqueRandomQuestions(db, 10)
	if err != nil {
		fmt.Println("Failed to fetch questions:", err)
		return
	}

	// Game logic
	score := 0

	for i, q := range questions {
		fmt.Printf("\nQuestion %d: %s (t/f): ", i+1, q.Question)

		userAnswer, _ := reader.ReadString('\n') // Read full input line safely
		userAnswer = strings.ToLower(strings.TrimSpace(userAnswer))

		// Check answer
		correct := (userAnswer == "t" && q.Answer) || (userAnswer == "f" && !q.Answer)
		if correct {
			fmt.Println("✅ Correct!")
			score++
		} else {
			fmt.Println("❌ Wrong!")
		}
	}

	fmt.Printf("\nGame over, %v! Your final score is: %d/%d\n", name, score, len(questions))
}
