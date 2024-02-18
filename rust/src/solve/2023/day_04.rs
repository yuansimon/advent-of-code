use std::collections::{HashMap, HashSet};
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
        4
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let mut sum = 0;
        for line in input.lines() {
            let wins = parse_line(debug, line);
            if wins > 0 {
                sum += 2u32.pow(wins - 1)
            }
        }
        sum.to_string()
    }

    fn part_two(debug: bool, input: &str) -> String {
        let num_cards = input.lines().count() as u32;
        let mut card_distribution: HashMap<u32, u32> = HashMap::new();
        (0..num_cards).for_each(|c| { card_distribution.insert(c, 1); });

        for (card, line) in input.lines().enumerate() {
            let card = card as u32;
            let amount = *card_distribution.get(&card).unwrap();
            let wins = parse_line(debug, line);
            for c in (card+1)..=(card + wins) {
                if let Some(&prev_value) = card_distribution.get(&c) {
                    card_distribution.insert(c, prev_value + amount);
                }
            };
        }
        card_distribution
            .values()
            .fold(0, |acc, v| acc + v)
            .to_string()
    }
}

fn parse_line(debug: bool, line: &str) -> u32 {
    let mut split = line.split(&[':', '|'][..]);
    let card = split.next().expect(&format!("Unexpected format (no card): {line}"));
    assert!(card.starts_with("Card "));
    let card: u32 = (&card[5..]).trim().parse().expect(&format!("Unexpected format (invalid card): {line}"));
    dprint!(debug, "Parsing Card {card}: ");
    let win_nums = split.next().expect(&format!("Unexpected format (no winning numbers): {line}"));
    let win_nums: HashSet<u32> = win_nums
        .split(" ")
        .into_iter()
        .filter(|&s| s != "")
        .map(|n| n.parse().expect(&format!("Unexpected format (invalid winning numbers): {line}")))
        .collect();
    let card_nums = split.next().expect(&format!("Unexpected format (no card numbers): {line}"));
    let card_nums: HashSet<u32> = card_nums
        .split(" ")
        .into_iter()
        .filter(|&s| s != "")
        .map(|n| n.parse().expect(&format!("Unexpected format (invalid card numbers): {line}")))
        .collect();

    dprint!(debug, "Win numbers: ");
    win_nums.iter().for_each(|n| dprint!(debug, "{n}; "));
    dprint!(debug, "Card numbers: ");
    card_nums.iter().for_each(|n| dprint!(debug, "{n}; "));
    dprintln!(debug, "");

    let wins = win_nums.intersection(&card_nums).count() as u32;
    dprintln!(debug, "Amount of winning numbers: {wins}");
    wins
}


struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
            Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
            Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
            Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "13"
    }

    fn get_part_one_real_output() -> &'static str {
        "20855"
    }

    fn get_part_two_example_input() -> &'static str {
        indoc! {"
            Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
            Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
            Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
            Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
            Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
            Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        "}
    }

    fn get_part_two_example_output() -> &'static str {
        "30"
    }

    fn get_part_two_real_output() -> &'static str {
        "5489600"
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
