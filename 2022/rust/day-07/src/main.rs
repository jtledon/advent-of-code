use nom::multi;

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

// $ command
//      cd
//      ls
// ls output
//      \d file
//      dir dirname

#[derive(Clone, Copy, Debug)]
struct File<'a> {
    filename: &'a str,
    size: u32
}

#[derive(Clone, Copy, Debug)]
struct Dir<'a> {
    dirname: &'a str,
}

#[derive(Clone, Copy, Debug)]
enum Command<'a> {
    LS,
    CD(&'a str)
}

#[derive(Clone, Copy, Debug)]
enum Line<'a> {
    FILE(File<'a>),
    DIR(Dir<'a>),
    COMMAND(Command<'a>)
}

fn parse_file_output(input: &str) -> nom::IResult<&str, Option<Line>> {
    let (input, filesize) = nom::character::complete::digit1(input)?;
    let size = str::parse::<u32>(filesize).ok().unwrap();
    // let (input, filesize) = nom::combinator::map_res(nom::character::complete::digit1, str::parse)?;
    let (input, _) = nom::character::complete::space1(input)?;
    let (input, filename) = nom::character::complete::not_line_ending(input)?;

    Ok((input, 
        Some(
            Line::FILE( File {
                filename, 
                size
            }))
        ))
}

fn parse_dir_output(input: &str) -> nom::IResult<&str, Option<Line>> {
    let (input, _) = nom::bytes::complete::tag("dir")(input)?;
    let (input, _) = nom::character::complete::space1(input)?;
    let (input, dirname) = nom::character::complete::alpha1(input)?;

    Ok((input, 
        Some(
            Line::DIR(Dir { 
                dirname 
            }))
        ))
}

fn parse_output(input: &str) -> nom::IResult<&str, Option<Line>> {
    let (input, file_dir) = nom::branch::alt((
                parse_file_output,
                parse_dir_output
            ))(input)?;
    Ok((input, file_dir))
}


// TO REMEMBER:
//      always have the `let (input, var)` as the assignment from every nom function
//      call the nom function with its full path to avoid using the wrong variation
//      dont forget to actually call the nom function on `(input)`
//      unwrap the nom function output with ?
//
//      Some function, such as alt, are expecting a single Tuple input and need (())
//      Make sure to return a Result type by returing Ok with a tuple containing the remaining
//          input and whatever res type your expecting
fn parse_command(input: &str) -> nom::IResult<&str, Option<Line>> {
    let (input, _) = nom::character::complete::char('$')(input)?;
    let (input, _) = nom::character::complete::space1(input)?;
    
    let (input, command_str) = nom::character::complete::alpha1(input)?;
    let res = match command_str {
        "cd" => {
            let (input, _) = nom::character::complete::space1(input)?;
            let (input, child_dir) = nom::character::complete::not_line_ending(input)?;
            
            // need to do full assignment here bc input doesnt get shadowed in outer scope
            Ok((input, Some( Line::COMMAND(Command::CD(child_dir)) ) ))
        },
        "ls" => Ok((input, Some( Line::COMMAND(Command::LS) ) )),
        _ =>    unreachable!()
    };
    res
}

fn parse_line(input: &str) -> nom::IResult<&str, Option<Line>> {
    let (input, line) = nom::branch::alt((
                parse_command,
                parse_output
            ))(input)?;
    Ok((input, line))
}

fn parse_data(input: &str) -> nom::IResult<&str, Vec<Option<Line>>> {
    let (input, lines) = multi::separated_list1(
            nom::character::complete::newline,
            parse_line
        )(input)?;
    for line in lines.clone() {
        println!("{:?}", line);
    }
    Ok((input, lines))
}

fn part1(data: &String) /* -> u32 */ {
    let _ = parse_data(data);
}


fn part2(data: &String) /* -> u32 */ {
}
