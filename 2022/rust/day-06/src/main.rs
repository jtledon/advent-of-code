use std::collections::{VecDeque, HashSet};

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

fn part1(data: &String) -> Option<u32> {
    let unique_count = 4;
    let mut q: VecDeque<char> = VecDeque::new();
    for (i, char) in data.chars().enumerate() {
        if HashSet::<&char>::from_iter(q.iter()).len() >= unique_count {
            return Some(i as u32);
        }

        if q.len() >= unique_count {
            q.pop_front();
        }
        q.push_back(char);
    }
    return None;
}


fn part2(data: &String) -> Option<u32> {
    let unique_count = 14;
    let mut q: VecDeque<char> = VecDeque::new();
    for (i, char) in data.chars().enumerate() {
        if HashSet::<&char>::from_iter(q.iter()).len() >= unique_count {
            return Some(i as u32);
        }

        if q.len() >= unique_count {
            q.pop_front();
        }
        q.push_back(char);
    }
    return None;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn first_test() {
        let data = "bvwbjplbgvbhsrlpgdmjqwftvncz".trim();
        let result = part1(&data.to_string());
        assert_eq!(result, Some(5) );
    }

    #[test]
    fn second_test() {
        let data = "nppdvjthqldpwncqszvftbrmjlhg".trim();
        let result = part1(&data.to_string());
        assert_eq!(result, Some(6) );
    }

    #[test]
    fn third_test() {
        let data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".trim();
        let result = part1(&data.to_string());
        assert_eq!(result, Some(10) );
    }

    #[test]
    fn fourth_test() {
        let data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".trim();
        let result = part1(&data.to_string());
        assert_eq!(result, Some(11) );
    }

    #[test]
    fn part2_first_test() {
        let data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb".trim();
        let result = part2(&data.to_string());
        assert_eq!(result, Some(19) );
    }

    #[test]
    fn part2_second_test() {
        let data = "bvwbjplbgvbhsrlpgdmjqwftvncz".trim();
        let result = part2(&data.to_string());
        assert_eq!(result, Some(23) );
    }

    #[test]
    fn part2_third_test() {
        let data = "nppdvjthqldpwncqszvftbrmjlhg".trim();
        let result = part2(&data.to_string());
        assert_eq!(result, Some(23) );
   
    }

    #[test]
    fn part2_fourth_test() {
        let data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg".trim();
        let result = part2(&data.to_string());
        assert_eq!(result, Some(29) );
   
    }

    #[test]
    fn part2_fifth_test() {
        let data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw".trim();
        let result = part2(&data.to_string());
        assert_eq!(result, Some(26) );

    }
    
}
