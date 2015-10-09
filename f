NSTimeInterval interval = [endDate timeIntervalSinceDate:startDate];
    if(interval < .0)
    {
        return nil;
    }

    int minutes = (int)(interval/60.0);

    if(interval < 3.0*60.0)
    {
        return @"Just now";
    }
    else if(interval < 30.0*60.0)
    {
        return [NSString stringWithFormat:@"%d minutes ago", minutes];
    }
    else if(interval < 60.0*60.0)
    {
        return @"Less then an hour ago";
    }
    else // go to hours
    {
        int hours = (int)(interval/(60.0*60.0));
        if(hours < 2)
        {
            return @"About an hour ago";
        }
        else if(hours <= 8)
        {
            return [NSString stringWithFormat:@"%d hours ago", hours];
        }
        else // go to days
        {
            NSDate *thisDate = [NSDate date];
            NSDate *castDate = [[NSDate date] dateByAddingTimeInterval:-interval];
            int days = (int)[self daysBetweenDate:castDate andDate:thisDate];
            if(days == 0)
            {
                return @"Today";
            }
            else if(days == 1)
            {
                return @"Yesterday";
            }
            else if(days <= 10)
            {
                return [NSString stringWithFormat:@"%d days ago", days];
            }
            else // go to months
            {
                int months = (int)[self monthsBetweenDate:castDate andDate:thisDate];
                if(months == 0)
                {
                    return @"This month";
                }
                else if(months == 1)
                {
                    return @"Last month";
                }
                else if(months <= 11)
                {
                    return [NSString stringWithFormat:@"%d months ago", months];
                }
                else // go to years
                {
                    int years = (int)[self yearsBetweenDate:castDate andDate:thisDate];
                    if(years == 0)
                    {
                        return @"This year";
                    }
                    else if(years == 1)
                    {
                        return @"Last years";
                    }
                    else
                    {
                        return [NSString stringWithFormat:@"%d years ago", months];
                    }
                }
            }
        }
    }
Add Comment Collapse