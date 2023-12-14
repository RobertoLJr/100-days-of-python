# Day 38 Project: Workout Tracking

## Concept

This program makes use of the Nutritionix API and the Sheety API with Google Sheets to work as a place to record
workouts using natural language. The user should first make sure to have valid keys in Nutritionix and Sheet before
using this program. Then, they can execute it as the following:

### Requirements

1. Nutritionix API App ID and Key (see resources).
2. A sheet in Google Sheets.
3. Sheety API data: username, project name, sheet name, and authentication credentials (if any).

### Usage

1. Provide the App ID and the App Key for Nutritionix as environment variables.
2. Provide the Sheety data as environment variables (username, project, sheet and token (if any)).
3. Then, whenever executing the program, the user can use natural language to record workout sessions. For example, when prompted for
`Tell me which exercises you did:`, the user can type `swam for 1 hour` or `walked for 30 minutes and ran for 30 minutes`.

After the input, them program should update the sheet with information about Date, Time, Exercise, Duration and Calories, automatically.

Note: doublecheck on Sheety the value for the sheet name because the API sometimes gives it a random arbitrary value
based on the sheet itself.

## Resources

### APIs

- [Nutritionix API Guide](https://developer.syndigo.com/docs/nutritionix-api-guide)
- [Sheety API Documentation](https://v2.sheety.co/docs/getting-started)

### Miscellanea

- [More about Nutritionix](https://www.nutritionix.com/)
