use std::fs;

#[derive(PartialEq, Debug, Clone)]
enum Hands {
    Rock = 0,
    Paper = 1,
    Scissor = 2
}

// I want to implement this because comparisons are circular but I want to be able to compare if
// one beats another
// impl PartialOrd for Hands {
//     fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
//         
//     }
// }

fn main() {
    let filepath: &str = "../../input-files/adventofcode.com_2022_day_2_input.txt";
    let data = read_data(filepath);
    let _ = part1(data.clone());

    let res = part2(data);
    println!("{:?}", res)
}

fn read_data(filepath: &str) -> String {
    return fs::read_to_string(filepath).ok().unwrap();
}

fn result_points(opponent_shape: &str, my_shape: &str) -> u32 {
    let o_shape: Hands = turn_into_enum(opponent_shape);
    let m_shape: Hands = turn_into_enum(my_shape);
    // A better way to do this would be to implement </=/> on the enum
    let win_res = match o_shape {
        Hands::Rock => {
            match m_shape {
                Hands::Rock => 3,
                Hands::Paper => 6,
                Hands::Scissor => 0,
            }    
        },
        Hands::Paper => {
            match m_shape {
                Hands::Rock => 0,
                Hands::Paper => 3,
                Hands::Scissor => 6,
            }    
        },
        Hands::Scissor => {
            match m_shape {
                Hands::Rock => 6,
                Hands::Paper => 0,
                Hands::Scissor => 3,
            }    
        },
    };
    // println!("{:?}, {:?}, {:?}", o_shape, m_shape, win_res);
    return win_res;
    
}

fn shape_points(shape_played: &str) -> u32{
    let shape: Hands = turn_into_enum(shape_played);
    let res = match shape {
        Hands::Rock => 1,
        Hands::Paper => 2,
        Hands::Scissor => 3,
    };
    // println!("{:?} => {:?}", shape_played, res);
    return res;
}

fn turn_into_enum(letter: &str) -> Hands {
    match letter {
        "A" | "X" => Hands::Rock,
        "B" | "Y" => Hands::Paper,
        "C" | "Z" => Hands::Scissor,
        _ => todo!()
    }
}

fn part1(data: String) -> u32 {
    let parsed: u32 = data
        .lines()
        .map(|line| {
            line
                .split(' ')
                .collect::<Vec<&str>>()
        })
        .map(|letters| {
             shape_points(letters[1]) + result_points(letters[0], letters[1])
        })
        .sum();

    dbg!(parsed);
    return parsed;
}

fn round2points(opponent_shape: &str, my_decision: &str) -> u32{
    let o_shape: Hands = turn_into_enum(opponent_shape);

    // println!("{:?}, {:?}, {:?}, {:?}", o_shape.clone(), o_shape.clone() as i32, (o_shape.clone() as i32) - 1, ((o_shape.clone() as i32) - 1).rem_euclid(3));

    let res = match my_decision {
        "X" => {0 + (((o_shape.clone() as i32) - 1).rem_euclid(3) + 1)}
        "Y" => {3 + (o_shape.clone() as i32) + 1}
        "Z" => {6 + (((o_shape.clone() as i32) + 1).rem_euclid(3) + 1)}
        _ => todo!()
    };
    // println!("{:?}, {:?}, {:?}", o_shape.clone(), my_decision, res);
    res.try_into().unwrap()
}

fn part2(data: String) -> u32 {
    data
        .lines()
        .map(|line| line.split(" ").collect::<Vec<&str>>())
        .map(|line| {
             round2points(line[0], line[1])
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ex_test() {
        let data = "
A Y
B X
C Z".trim();
        let result = part1(data.to_string());
        assert_eq!(result, 15);
    }
}
