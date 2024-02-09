use std::error::Error;
use std::fs;
use std::fs::File;
use std::io::Read;
use std::path::Path;

use reqwest;
use reqwest::header::COOKIE;

const BASE_AOC_URL: &str = "https://adventofcode.com";
const PATH_TO_SESSION_COOKIE_TXT: &str = "src/aoc/session_cookie.txt";
const PATH_TO_INPUTS_DIR: &str = "inputs";

fn read_cookie_file() -> std::io::Result<String> {
    let mut f = File::open(PATH_TO_SESSION_COOKIE_TXT)?;
    let mut data = String::from("");
    f.read_to_string(&mut data)?;
    Ok(data)
}

fn write_input_file(input: &str, year: u32, day: u32) -> Result<(), Box<dyn Error>> {
    let path_to_inputs_year_dir: &str = &format!("{PATH_TO_INPUTS_DIR}/{year}");
    let path_to_input: &str = &format!("{path_to_inputs_year_dir}/day_{day:02}.txt");

    if !Path::new(PATH_TO_INPUTS_DIR).exists() {
        fs::create_dir(PATH_TO_INPUTS_DIR)?;
    }
    if !Path::new(path_to_inputs_year_dir).exists() {
        fs::create_dir(path_to_inputs_year_dir)?;
    }
    fs::write(path_to_input, input)?;
    Ok(())
}


async fn get_request(url: String) -> Result<String, Box<dyn Error>> {
    let session_cookie = login();

    println!("Get request to url: {url}");

    let client = reqwest::Client::new();

    let response = client
        .get(url)
        .header(COOKIE, format!("session={session_cookie}"))
        .send()
        .await?
        .text()
        .await?;

    Ok(response)
}

fn login() -> String {
    let session_cookie: String;

    match read_cookie_file() {
        Ok(cookie) => session_cookie = cookie,
        Err(err) => {
            eprintln!("Encountered File Error: \n{:?}", err);
            open_browser();
            panic!("Log In And Update session_cookie.txt")
        }
    };

    session_cookie
}

fn open_browser() {
    let path = format!("{BASE_AOC_URL}");

    match open::that(&path) {
        Ok(()) => println!("Successfully opened browser at '{}'", path),
        Err(err) => eprintln!("An error occurred when opening browser at '{}':\n{}", path, err),
    }
}

fn read_input(year: u32, day: u32) -> Result<String, Box<dyn Error>> {
    let path_to_inputs_year_dir: &str = &format!("{PATH_TO_INPUTS_DIR}/{year}/day_{day:02}.txt");
    let mut f = File::open(path_to_inputs_year_dir)?;
    let mut input = String::from("");
    f.read_to_string(&mut input)?;
    Ok(input)
}

pub async fn fetch_input(year: u32, day: u32) -> Result<(), Box<dyn Error>> {
    match (day, year) {
        (1..=25, 2015..) => (),
        _ => return Err(Box::from("Invalid year or day")),
    }

    let url = format!("{BASE_AOC_URL}/{year}/day/{day}/input");

    let input = get_request(url).await?;

    println!("Fetched input for year {year} day {day}.");

    write_input_file(&input, year, day)
}

pub async fn read_or_fetch_input(year: u32, day: u32) -> Result<String, Box<dyn Error>> {
    let path_to_inputs_year_dir: &str = &format!("{PATH_TO_INPUTS_DIR}/{year}/day_{day:02}.txt");
    if !Path::new(path_to_inputs_year_dir).exists() {
        fetch_input(year, day).await?
    };
    read_input(year, day) as Result<String, Box<dyn Error>>
}