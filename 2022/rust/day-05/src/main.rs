use std::{vec, cmp::Reverse};
use nom::{
    IResult 
};

fn main() {
    let data = read_data();
    println!("{:?}", part1(&data));
    println!("{:?}", part2(&data));
}

fn get_file_name() -> String {
    let cwd = std::env::current_dir().ok().unwrap();
    let cwd_str = cwd.to_str().unwrap();

    let re = regex::Regex::new(r"(^.*)/(\d{4})/.*/day-(\d+).*$").unwrap();
    let cap = re.captures(cwd_str).unwrap();
    let leading_dir = cap.get(1).unwrap().as_str();
    let year = cap.get(2).unwrap().as_str();
    let day = cap.get(3).unwrap().as_str().trim_start_matches('0');

    let path = std::path::Path::new(".")
                    .join(leading_dir)
                    .join(year)
                    .join("input-files")
                    .join(format!("adventofcode.com_{year}_day_{day}_input.txt"));
    assert!(path.exists());
    let path_str = path.to_str().unwrap();

    return String::from(path_str);
    
}

fn read_data() -> String {
    let filepath = get_file_name();
    return std::fs::read_to_string(filepath).ok().unwrap();
}

fn parse_crate(input: &str) -> IResult<&str, Option<&str>> {
    let (input, crt) = 
        nom::branch::alt((
                nom::bytes::complete::tag("   "),
                nom::sequence::delimited(
                    nom::character::complete::char('['),
                    nom::character::complete::alpha1,
                    nom::character::complete::char(']'),
                )
        ))(input)?;

    let res = match crt {
        "   " => None,
        x => Some(x)
    };
    Ok((input, res))
}

fn parse_line(input: &str) -> IResult<&str, Vec<Option<&str>>> {
    let (input, line) = nom::multi::separated_list1(
            nom::character::complete::char(' '),
            parse_crate
        )(input)?;
    Ok((input, line))
}

fn horizontal_crates(input: &str) -> IResult<&str, Vec< Vec<Option <&str> > > > {
    let (input, res) = nom::multi::separated_list1(
            nom::character::complete::newline,
            parse_line
        )(input)?;
    Ok((input, res))
}

fn horizontal_to_vertical_stacks(horizontal: Vec<Vec<Option<&str>>>) -> Vec<Vec<&str>>{
    // println!("{horizontal:#?}");
    let mut agg = vec![];
    for j in 0..horizontal[0].len() {
        let mut vertical_stack = vec![];
        for i in 0..horizontal.len() {
           match horizontal[i][j] {
                Some(x) => vertical_stack.push(x),
                None => (),
           }
        }
        vertical_stack.reverse();
        agg.push(vertical_stack);
    }

    // dbg!(agg.clone());
    agg
}

#[derive(Debug)]
struct Command {
    repetition: u8,
    from: u8,
    to: u8
}

fn parse_command(input: &str) -> IResult<&str, Command> {
    let (input, _) = nom::bytes::complete::tag("move ")(input)?;
    let (input, repetition) = nom::character::complete::u8(input)?;
    let (input, _) = nom::bytes::complete::tag(" from ")(input)?;
    let (input, from) = nom::character::complete::u8(input)?;
    let (input, _) = nom::bytes::complete::tag(" to ")(input)?;
    let (input, to) = nom::character::complete::u8(input)?;
    Ok((input, Command { repetition, from, to } ))
}

fn parse_commands(input: &str) -> IResult<&str, Vec<Command>> {
    let (input, res) = nom::multi::separated_list1(
            nom::character::complete::newline,
            parse_command
        )(input)?;
    Ok((input, res))
}

fn part1(data: &String) {

    let input_sections = data.split("\n\n").collect::<Vec<&str>>();
    let mut stacks_input = input_sections[0];
    stacks_input = &stacks_input[..stacks_input.len()-1];
    let commands_input = input_sections[1];

    let horizontal_stacks = horizontal_crates(stacks_input).ok().unwrap().1;
    let mut stacks = horizontal_to_vertical_stacks(horizontal_stacks);

    let commands = parse_commands(commands_input).ok().unwrap().1;
    
    for command in commands {
        // println!("{command:?}");
        for _ in 0..command.repetition {
            let val = stacks[command.from as usize - 1].pop().unwrap();
            stacks[command.to as usize - 1].push(val);
        }
    }

    stacks.iter().for_each(|stack| print!("{}", stack[stack.len()-1]));
    println!();
}


fn part2(data: &String) /* -> u32 */ {
}
