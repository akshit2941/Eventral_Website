class ArtistStats:
    def __init__(self, followers_growth, profile_views, concerts, content_engagement):
        self.followers_growth = followers_growth
        self.profile_views = profile_views
        self.concerts = concerts
        self.content_engagement = content_engagement

    def calculate_metrics(self):
        # Total revenue, total ticket sold, ticket revenue, current reach
        total_revenue = sum([concert['Revenue'] for concert in self.concerts])
        total_tickets_sold = sum([concert['Registered'] for concert in self.concerts])
        ticket_revenue = sum([concert['Revenue'] for concert in self.concerts])
        current_reach = self.followers_growth[-1]

        # Comparing data from last month
        last_month = self.concerts[-1]
        last_month_ticket_sold = last_month['Registered']
        last_month_refunded_tickets = last_month['Refunded Tickets']
        last_month_attended = last_month['Attended']
        last_month_growth_ticket_sold = ((total_tickets_sold - last_month_ticket_sold) / last_month_ticket_sold) * 100
        last_month_growth_refunded_tickets = ((last_month_refunded_tickets) / last_month_ticket_sold) * 100
        last_month_growth_attended = ((last_month_attended) / last_month_ticket_sold) * 100

        # Content engagement metrics
        content_views = sum([month['Total Views'] for month in self.content_engagement])
        content_likes = sum([month['Total Likes'] for month in self.content_engagement])
        content_comments = sum([month['Total Comments'] for month in self.content_engagement])
        content_engagement = sum([month['Total Engagement'] for month in self.content_engagement])
        content_interaction_rate = (content_engagement / content_views) * 100
        content_saved = 5000  # Assume a constant number of saved content for demonstration

        return {
            "Total Revenue": total_revenue,
            "Total Tickets Sold": total_tickets_sold,
            "Ticket Revenue": ticket_revenue,
            "Current Reach": current_reach,
            "Last Month Ticket Sold": last_month_ticket_sold,
            "Last Month Refunded Tickets": last_month_refunded_tickets,
            "Last Month Attended": last_month_attended,
            "Last Month Growth in Ticket Sold (%)": last_month_growth_ticket_sold,
            "Last Month Growth in Refunded Tickets (%)": last_month_growth_refunded_tickets,
            "Last Month Growth in Attended (%)": last_month_growth_attended,
            "Content Views": content_views,
            "Content Likes": content_likes,
            "Content Comments": content_comments,
            "Content Engagement": content_engagement,
            "Content Interaction Rate (%)": content_interaction_rate,
            "Content Saved": content_saved
        }


# Sample data
followers_growth = [20000, 21500, 22800, 24000, 25200, 27000, 29500, 32000, 35000, 38500, 42000, 46000]
profile_views = [15000, 16200, 17500, 18800, 20000, 22000, 25000, 28000, 32000, 36000, 40000, 45000]

concerts = [
    {"Registered": 1500, "Attended": 1200, "Revenue": 60000, "Refunded Tickets": 50},
    {"Registered": 3000, "Attended": 2800, "Revenue": 140000, "Refunded Tickets": 100},
    {"Registered": 6500, "Attended": 4800, "Revenue": 170000, "Refunded Tickets": 20},
    {"Registered": 8000, "Attended": 5800, "Revenue": 140000, "Refunded Tickets": 100},
    {"Registered": 7000, "Attended": 800, "Revenue": 148000, "Refunded Tickets": 40},
    {"Registered": 3000, "Attended": 2800, "Revenue": 140000, "Refunded Tickets": 70},
    {"Registered": 5000, "Attended": 3800, "Revenue": 170000, "Refunded Tickets": 50},
    {"Registered": 6000, "Attended": 1800, "Revenue": 90000, "Refunded Tickets": 80}
]

content_engagement = [
    {"Total Views": 50000, "Total Likes": 5000, "Total Comments": 500, "Total Engagement": 5500},
    {"Total Views": 60000, "Total Likes": 6500, "Total Comments": 600, "Total Engagement": 7100},
    {"Total Views": 55000, "Total Likes": 6000, "Total Comments": 550, "Total Engagement": 6550},
    {"Total Views": 50000, "Total Likes": 5500, "Total Comments": 600, "Total Engagement": 6100},
    {"Total Views": 55000, "Total Likes": 6200, "Total Comments": 650, "Total Engagement": 6850},
    {"Total Views": 60000, "Total Likes": 6800, "Total Comments": 700, "Total Engagement": 7500},
    {"Total Views": 65000, "Total Likes": 7000, "Total Comments": 750, "Total Engagement": 7750},
    {"Total Views": 62000, "Total Likes": 7200, "Total Comments": 800, "Total Engagement": 8000},
    {"Total Views": 60000, "Total Likes": 7500, "Total Comments": 850, "Total Engagement": 8350},
    {"Total Views": 58000, "Total Likes": 7800, "Total Comments": 900, "Total Engagement": 8700},
    {"Total Views": 60000, "Total Likes": 8000, "Total Comments": 950, "Total Engagement": 8950},
    {"Total Views": 65000, "Total Likes": 8500, "Total Comments": 1000, "Total Engagement": 9500}
]

# Create an instance of ArtistStats
artist_stats = ArtistStats(followers_growth, profile_views, concerts, content_engagement)

# Calculate metrics
metrics = artist_stats.calculate_metrics()

# Output results
for key, value in metrics.items():
    print(f"{key}: {value}")
