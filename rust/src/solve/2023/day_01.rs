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
        false
    }

    fn part_one(debug: bool, input: &str) -> String {
        let mut sum = 0u32;
        for line in input.lines() {
            let mut first_digit = None;
            let mut last_digit = None;
            for char in line.chars() {
                if let Some(digit) = char.to_digit(10) {
                    if first_digit.is_none() {
                        first_digit = Some(digit);
                    }
                    last_digit = Some(digit);
                }
            }
            let first_digit = first_digit
                .expect(&format!("no digits found in line {}", line))
                .to_string();
            let last_digit = last_digit.unwrap().to_string();

            let number: u32 = format!("{first_digit}{last_digit}").parse().unwrap();
            dprintln!(debug, "found number: {number}");
            sum += number;
        };
        dprintln!(debug, "Result: {sum}");
        sum.to_string()
    }

    fn part_two(debug: bool, input: &str) -> String {
        todo!()
    }
}

struct TestCases;

impl TestCaseProvider for TestCases {
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
        ""
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        TestCases::test_part_one_example::<Solve>();
    }

    #[test]
    fn test_part_one_real() {
        TestCases::test_part_one_real::<Solve>();
    }

    #[test]
    fn test_part_two_example() {
        TestCases::test_part_two_example::<Solve>();
    }

    #[test]
    fn test_part_two_real() {
        TestCases::test_part_two_real::<Solve>();
    }
}
