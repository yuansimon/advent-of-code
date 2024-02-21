use indoc::indoc;

use crate::dprintln;
use crate::solve::{Solver, TestCaseProvider};

pub struct Solve;

impl Solver for Solve {
    fn get_year() -> u32 {
        2023
    }

    fn get_day() -> u32 {
        6
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let (times, distances) = parse(debug, input);
        solve(debug, times, distances)
    }

    fn part_two(debug: bool, input: &str) -> String {
        let (times, distances) = parse(debug, input);
        let time = times.iter()
            .fold("".to_string(), |prefix, time| format!("{prefix}{time}"))
            .parse()
            .unwrap();
        let distance = distances.iter()
            .fold("".to_string(), |prefix, distance| format!("{prefix}{distance}"))
            .parse()
            .unwrap();
        solve(debug, vec![time], vec![distance])
    }
}

fn solve(debug: bool, times: Vec<u64>, distances: Vec<u64>) -> String {
    let result: u32 = times.iter()
        .zip(distances.iter())
        .map(|(time, dist)| {
            let time = *time as f64;
            let dist = *dist as f64;
            let sqrt_res = (time * time - 4.0 * dist).sqrt();
            let x1 = (time - sqrt_res) / 2.0;
            let x2 = (time + sqrt_res) / 2.0;
            let left = (x1.min(x2) + 1.0).floor() as u32;
            let right = (x1.max(x2) - 1.0).ceil() as u32;
            let result = right - left + 1;
            dprintln!(debug, "Computed extreme points for time={time} distance={dist} => {left} - {right} => {result}");
            result
        })
        .reduce(|acc, num_wins| acc * num_wins)
        .unwrap();
    result.to_string()
}

fn parse(debug: bool, input: &str) -> (Vec<u64>, Vec<u64>) {
    let mut lines = input.lines();
    let line = lines.next().unwrap();
    assert!(line.starts_with("Time:"));
    let times: Vec<u64> = (line[5..]).split(" ")
        .filter(|&s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect();

    let line = lines.next().unwrap();
    assert!(line.starts_with("Distance:"));
    let distances: Vec<u64> = (line[9..]).split(" ")
        .filter(|&s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect();

    assert_eq!(times.len(), distances.len());
    dprintln!(debug, "Times: {:?}", times);
    dprintln!(debug, "Distances: {:?}", distances);
    (times, distances)
}

struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            Time:      7  15   30
            Distance:  9  40  200
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "288"
    }

    fn get_part_one_real_output() -> &'static str {
        "449550"
    }

    fn get_part_two_example_input() -> &'static str {
        Self::get_part_one_example_input()
    }

    fn get_part_two_example_output() -> &'static str {
        "71503"
    }

    fn get_part_two_real_output() -> &'static str {
        "28360140"
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
        TestCases::test_part_two_real(true);
    }
}
