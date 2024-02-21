use indoc::indoc;

use crate::{dprint, dprintln};
use crate::solve::{Solver, TestCaseProvider};
use crate::utils::Range;

pub struct Solve;

impl Solver for Solve {
    fn get_year() -> u32 {
        2023
    }

    fn get_day() -> u32 {
        5
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let (seeds, translations) = parse(debug, input);
        seeds.iter()
            .map(|&seed| translate_seed(debug, seed, &translations))
            .min()
            .unwrap()
            .to_string()
    }

    fn part_two(debug: bool, input: &str) -> String {
        let (seeds, translations) = parse(debug, input);
        let mut seed_ranges = vec![];
        assert_eq!(seed_ranges.len() % 2, 0);
        let mut iterator = seeds.iter();
        while let Some(seed) = iterator.next() {
            let seed = *seed as i64;
            let range = *iterator.next().unwrap() as i64;
            seed_ranges.push(Range::new(seed, seed + range - 1).unwrap())
        }

        translate_seeds(debug, seed_ranges, &translations).iter()
            .reduce(|range_a, range_b| if range_a.get_left() < range_b.get_left() { range_a } else { range_b })
            .unwrap()
            .get_left()
            .to_string()
    }
}

type TranslationRange = (Range, i64);

fn translate_seeds(debug: bool, seed_ranges: Vec<Range>, translations: &Vec<Vec<TranslationRange>>) -> Vec<Range> {
    let result = translations.iter().enumerate().fold(seed_ranges, |input_ranges, (index, translation_range)| {
        dprintln!(debug, "Translating input_ranges at level {index}: {}", Range::format_vec(&input_ranges));
        let result = input_ranges.iter()
            .flat_map(|input_range| translate_range(debug, input_range, translation_range))
            .collect();
        result
    });
    dprintln!(debug, "");
    result
}

fn translate_range(debug: bool, input_range: &Range, translation_ranges: &Vec<TranslationRange>) -> Vec<Range> {
    dprintln!(debug, "\tTranslating {}:", input_range);
    let mut current_range = Some(input_range.clone());
    let result: Vec<Range> = translation_ranges.iter().enumerate().flat_map(|(index, (tr, offset))| {
        if let Some(ref range_to_intersect) = current_range {
            let (left, intersect, right) = range_to_intersect.intersect_other(tr);
            let translated = intersect.map(|range| range.translate(*offset));

            dprintln!(debug, "\t\tIntersect {} with {}+{} => ({},{},{})",
                range_to_intersect, tr, offset,
                Range::format_option(&left), Range::format_option(&translated), Range::format_option(&right));

            current_range = right.clone();
            let include_right = if index == translation_ranges.len() - 1 {
                Some(right).flatten()
            } else {
                None
            };
            let result: Vec<Range> = vec![left, translated, include_right].into_iter()
                .flatten()
                .collect();
            result
        } else {
            vec![]
        }
    }).collect();
    dprintln!(debug, "\tTranslated {} to {}", input_range, Range::format_vec(&result));
    result
}

fn translate_seed(debug: bool, seed: u32, translations: &Vec<Vec<TranslationRange>>) -> u32 {
    dprint!(debug, "Translating {seed}");
    let result = translations.iter().fold(seed as i64, |input, range| {
        translate(debug, input, range)
    }) as u32;
    dprintln!(debug, "");
    result
}

fn translate(debug: bool, input: i64, ranges: &Vec<TranslationRange>) -> i64 {
    let result = match ranges.iter().find(|&(range, _)| range.contains(input)) {
        None => input,
        Some((_, offset)) => input + offset
    };
    dprint!(debug, " => {result}");
    result
}

fn parse(debug: bool, input: &str) -> (Vec<u32>, Vec<Vec<TranslationRange>>) {
    let mut lines = input.lines()
        .into_iter()
        .filter(|&line| line != "")
        .map(|line| line.trim());
    let seeds = lines.next().expect("Unexpected format (no seeds)");
    assert!(seeds.starts_with("seeds: "));
    let seeds: Vec<u32> = seeds.split(" ")
        .into_iter()
        .map(|seed| seed.parse::<u32>())
        .flatten()
        .collect();
    dprintln!(debug, "Parsed Seeds: {:?}", seeds);

    let mut acc = vec![];
    let mut translations = vec![];
    while let Some(line) = lines.next() {
        acc = parse_line(debug, line, acc.clone(), &mut translations);
    }
    acc.sort_by_key(|(range, _)| range.get_left());
    translations.push(acc);
    dprintln!(debug, "");
    (seeds, translations)
}

fn parse_line(debug: bool, line: &str, mut acc: Vec<TranslationRange>, translations: &mut Vec<Vec<TranslationRange>>) -> Vec<TranslationRange> {
    if line.ends_with("map:") {
        dprintln!(debug, "Parsing {line}");
        if !acc.is_empty() {
            acc.sort_by_key(|(range, _)| range.get_left());
            translations.push(acc);
        }
        return vec![];
    }

    let mut split = line.trim().split(" ");
    let destination = split.next()
        .map(|source| source.parse::<u32>().ok())
        .flatten()
        .expect(&format!("Unexpected format (destination): {line}")) as i64;
    let source = split.next()
        .map(|source| source.parse::<u32>().ok())
        .flatten()
        .expect(&format!("Unexpected format (source): {line}")) as i64;
    let range_length = split.next()
        .map(|source| source.parse::<u32>().ok())
        .flatten()
        .expect(&format!("Unexpected format (range length): {line}")) as i64;
    assert!(split.next().is_none());

    dprint!(debug, "{destination} {source} {range_length}: ");
    let tr: TranslationRange = (Range::new(source, source + range_length - 1).unwrap(), destination - source);
    dprintln!(debug, "({}, {})", tr.0, tr.1);
    acc.push(tr);
    acc
}


struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            seeds: 79 14 55 13

            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "35"
    }

    fn get_part_one_real_output() -> &'static str {
        "424490994"
    }

    fn get_part_two_example_input() -> &'static str {
        Self::get_part_one_example_input()
    }

    fn get_part_two_example_output() -> &'static str {
        "46"
    }

    fn get_part_two_real_output() -> &'static str {
        "15290096"
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
