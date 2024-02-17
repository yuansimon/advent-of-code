use indoc::indoc;

use crate::dprint;
use crate::dprintln;
use crate::solve::{Solver, TestCaseProvider};

pub struct Solve;

impl Solver for Solve {
    fn get_year() -> u32 {
        2023
    }

    fn get_day() -> u32 {
        2
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let mut id_sum = 0;
        for line in input.lines() {
            let (id, sets) = parse_line(debug, line);
            let valid_set = sets.into_iter().all(
                |(r, g, b)| r <= 12 && g <= 13 && b <= 14
            );
            if valid_set {
                dprintln!(debug, "Game {id} is valid.");
                id_sum += id
            };
        }
        id_sum.to_string()
    }

    fn part_two(debug: bool, input: &str) -> String {
        let mut power_sum = 0;
        for line in input.lines() {
            let (id, sets) = parse_line(debug, line);
            let min_set = sets.into_iter().reduce(
                |(acc_r, acc_g, acc_b), (r, g, b)| (acc_r.max(r), acc_g.max(g), acc_b.max(b))
            ).expect(&format!("Unexpected empty sets for game {id}"));
            let power = min_set.0 * min_set.1 * min_set.2;
            power_sum += power;
            dprintln!(debug, "Game {id} has minimal set {:?} and power {power}", min_set)
        }
        power_sum.to_string()
    }
}

type Id = u32;

type Set = (u32, u32, u32);

fn parse_set(debug: bool, unparsed_set: &str) -> Set {
    let mut split = unparsed_set.trim().split(",");
    let mut set: Set = (0u32, 0u32, 0u32);
    while let Some(unparsed_color) = split.next() {
        let mut inner_split = unparsed_color.trim().split(" ");
        let value: u32 = inner_split.next()
            .expect(&format!("Unexpected format (no color value): {:?}", set))
            .parse()
            .expect(&format!("Unexpected format (invalid color value): {:?}", set));
        let color = inner_split.next()
            .expect(&format!("Unexpected format (no color): {:?}", set));
        let color_name: &str = &color.trim().to_lowercase();
        match color_name {
            "red" => set.0 = value,
            "green" => set.1 = value,
            "blue" => set.2 = value,
            _ => panic!("Unexpected format (invalid color name): {:?}", set)
        }
    }
    dprint!(debug, "({}, {}, {}); ", set.0, set.1, set.2);
    set
}

fn parse_line(debug: bool, line: &str) -> (Id, Vec<Set>) {
    let mut split = line.split(&[':', ';'][..]);
    let unparsed_id = split.next().expect(&format!("Unexpected format (no id): {line}"));
    assert!(unparsed_id.starts_with("Game "));
    let id: Id = (&unparsed_id[5..] as &str).parse().expect(&format!("Unexpected format (invalid id): {line}"));
    dprint!(debug, "Parsing Game {id}: ");
    let mut sets: Vec<Set> = vec![];
    for unparsed_set in split {
        sets.push(parse_set(debug, unparsed_set));
    }
    dprintln!(debug,"");
    (id, sets)
}

struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "8"
    }

    fn get_part_one_real_output() -> &'static str {
        "2207"
    }

    fn get_part_two_example_input() -> &'static str {
        indoc! {"
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        "}
    }

    fn get_part_two_example_output() -> &'static str {
        "2286"
    }

    fn get_part_two_real_output() -> &'static str {
        "62241"
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
