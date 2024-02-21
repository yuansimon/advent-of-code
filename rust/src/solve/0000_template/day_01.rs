use indoc::indoc;

use crate::dprint;
use crate::dprintln;
use crate::solve::{Solver, TestCaseProvider};

pub struct Solve;

impl Solver for Solve {
    fn get_year() -> u32 {
        0000
    }

    fn get_day() -> u32 {
        0
    }

    fn is_part_one_solved() -> bool {
        false
    }

    fn is_part_two_solved() -> bool {
        false
    }

    fn part_one(debug: bool, input: &str) -> String {
        dprint!(debug, "{input}");
        panic!("not yet implemented");
    }

    fn part_two(debug: bool, input: &str) -> String {
        dprintln!(debug, "{input}");
        panic!("not yet implemented");
    }
}

struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            a
            b
            c
            d
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        ""
    }

    fn get_part_one_real_output() -> &'static str {
        ""
    }

    fn get_part_two_example_input() -> &'static str {
        indoc! {"
            1
            2
            3
            4
        "}
    }

    fn get_part_two_example_output() -> &'static str {
        ""
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
