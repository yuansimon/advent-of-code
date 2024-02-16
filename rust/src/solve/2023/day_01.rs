use std::error::Error;
use indoc::indoc;

use crate::dprintln;
use crate::solve::TestCaseProvider;

pub struct Solve;

impl super::Solver for Solve {
    fn get_year() -> u32 {
        2023
    }

    fn get_day() -> u32 {
        1
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let digits = vec!["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        let digits: Vec<(usize, &str)> = digits.into_iter().enumerate().collect();
        solve(debug, input, digits)
    }

    fn part_two(debug: bool, input: &str) -> String {
        let digit_names = vec!["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
        let digit_names: Vec<(usize, &str)> = digit_names.into_iter().enumerate().collect();
        let digits = vec!["1", "2", "3", "4", "5", "6", "7", "8", "9"];
        let digits: Vec<(usize, &str)> = digits.into_iter().enumerate().collect();
        let mut all_digits: Vec<(usize, &str)> = vec![];
        all_digits.extend(digits);
        all_digits.extend(digit_names);
        solve(debug, input, all_digits)
    }
}


fn solve(debug: bool, input: &str, all_digits: Vec<(usize, &str)>) -> String {
    let mut sum = 0u32;
    for line in input.lines() {
        let first_digit: usize = all_digits
            .iter()
            .map(|&(value, digit)| line.find(digit).map(|pos| (value, pos)))
            .flatten()
            .min_by_key(|&(_, pos)| pos)
            .map(|(value, _)| value + 1)
            .expect(&format!("Unexpected input line without any digits: {line}"));

        let last_digit: usize = all_digits
            .iter()
            .map(|&(value, digit)| line.rfind(digit).map(|pos| (value, pos)))
            .flatten()
            .max_by_key(|&(_, pos)| pos)
            .map(|(value, _)| value + 1)
            .expect(&format!("Unexpected input line without any digits: {line}"));

        let number: u32 = format!("{first_digit}{last_digit}").parse().unwrap();
        dprintln!(debug, "found number: {number}");
        sum += number;
    };
    sum.to_string()
}


struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "142"
    }

    fn get_part_one_real_output() -> &'static str {
        "53974"
    }

    fn get_part_two_example_input() -> &'static str {
        indoc! {"
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
        "}
    }

    fn get_part_two_example_output() -> &'static str {
        "281"
    }

    fn get_part_two_real_output() -> &'static str {
        "52840"
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        TestCases::test_part_one_example(true);
    }

    #[test]
    fn test_part_one_real() {
        TestCases::test_part_one_real(false);
    }

    #[test]
    fn test_part_two_example() {
        TestCases::test_part_two_example(true);
    }

    #[test]
    fn test_part_two_real() {
        TestCases::test_part_two_real(false);
    }
}
