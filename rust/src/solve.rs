use std::error::Error;

use futures::executor::block_on;

pub use y2023d01::Solve as day_01;

use crate::aoc::helper::read_or_fetch_input;
use crate::utils::print_hr;

#[path = "solve/2023/day_01.rs"]
mod y2023d01;

pub trait Solver {
    fn get_year() -> u32;
    fn get_day() -> u32;
    fn is_part_one_solved() -> bool;
    fn is_part_two_solved() -> bool;
    fn part_one(debug: bool, input: &str) -> String;
    fn part_two(debug: bool, input: &str) -> String;
    fn solve_part_one() -> Result<String, Box<dyn Error>> {
        if !Self::is_part_one_solved() {
            let err = format!("Solver for {} Day {:02} Part 1 not marked as solved.", Self::get_year(), Self::get_day());
            eprintln!("{err}");
            return Err(Box::from(err));
        }
        let input = block_on(read_or_fetch_input(Self::get_year(), Self::get_day()))?;
        let result = Self::part_one(false, &input);
        println!("Solved AoC {} Day {:02} Part 1: {result}", Self::get_year(), Self::get_day());
        Ok(result)
    }

    fn solve_part_two() -> Result<String, Box<dyn Error>> {
        if !Self::is_part_two_solved() {
            let err = format!("Solver for {} Day {:02} Part 2 not marked as solved.", Self::get_year(), Self::get_day());
            eprintln!("{err}");
            return Err(Box::from(err));
        }
        let input = block_on(read_or_fetch_input(Self::get_year(), Self::get_day()))?;
        let result = Self::part_two(false, &input);
        println!("Solved AoC {} Day {:02} Part 2: {result}", Self::get_year(), Self::get_day());
        Ok(result)
    }
}

pub trait TestCaseProvider<S: Solver> {
    fn get_part_one_example_input() -> &'static str;
    fn get_part_one_example_output() -> &'static str;
    fn get_part_one_real_output() -> &'static str;
    fn get_part_two_example_input() -> &'static str;
    fn get_part_two_example_output() -> &'static str;
    fn get_part_two_real_output() -> &'static str;
    fn test_part_one_example(debug: bool) {
        let input = Self::get_part_one_example_input();
        let output = Self::get_part_one_example_output();
        println!("Running Part 1 Test on example input and expecting output [{output}]: \n{input}");
        let result = S::part_one(debug, input);
        print_hr(false);
        println!("Resulting output [{result}]. Expecting output [{output}]");
        print_hr(true);
        assert_eq!(result, output);
    }
    fn test_part_one_custom(debug: bool, input: &str, output: &str) {
        println!("Running Part 1 Test on custom input and expecting output [{output}]: \n{input}");
        let result = S::part_one(debug, input);
        print_hr(false);
        println!("Resulting output [{result}]. Expecting output [{output}]");
        print_hr(true);
        assert_eq!(result, output);
    }
    fn test_part_one_real(debug: bool) {
        if S::is_part_one_solved() {
            let input = block_on(read_or_fetch_input(S::get_year(), S::get_day())).unwrap();
            let output = Self::get_part_one_real_output();
            println!("Running Part 1 Test on real input and expecting output [{output}]");
            let result = S::part_one(debug, &input);
            print_hr(false);
            println!("Resulting output [{result}]. Expecting output [{output}]");
            print_hr(true);
            assert_eq!(result, Self::get_part_one_real_output());
        } else {
            println!("Skipping Test")
        }
    }
    fn test_part_two_example(debug: bool) {
        if S::is_part_one_solved() {
            let input = Self::get_part_two_example_input();
            let output = Self::get_part_two_example_output();
            println!("Running Part 2 Test on example input and expecting output [{output}]: \n{input}");
            let result = S::part_two(debug, input);
            print_hr(false);
            println!("Resulting output [{result}]. Expecting output [{output}]");
            print_hr(true);
            assert_eq!(result, output);
        } else {
            println!("Skipping Test")
        }
    }
    fn test_part_two_custom(debug: bool, input: &str, output: &str) {
        if S::is_part_one_solved() {
            println!("Running Part 2 Test on custom input and expecting output [{output}]: \n{input}");
            let result = S::part_two(debug, input);
            print_hr(false);
            println!("Resulting output [{result}]. Expecting output [{output}]");
            print_hr(true);
            assert_eq!(result, output);
        } else {
            println!("Skipping Test")
        }
    }
    fn test_part_two_real(debug: bool) {
        if S::is_part_one_solved() && S::is_part_two_solved() {
            let input = block_on(read_or_fetch_input(S::get_year(), S::get_day())).unwrap();
            let output = Self::get_part_two_real_output();
            println!("Running Part 2 Test on real input and expecting output [{output}]");
            let result = S::part_two(debug, &input);
            print_hr(false);
            println!("Resulting output [{result}]. Expecting output [{output}]");
            print_hr(true);
            assert_eq!(result, output);
        } else {
            println!("Skipping Test")
        }
    }
}
