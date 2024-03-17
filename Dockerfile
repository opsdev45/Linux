# Use a base image that includes Bash
FROM alpine:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the Bash script into the container
COPY log_err.sh .

# Install cron
RUN apk --no-cache add dcron

# Give execute permission to the Bash script
RUN chmod +x log_err.sh

# Run cron in the foreground with the crontab entry to execute the script every minute
CMD ["crond", "-f", "-d", "8", "-l", "8", "-L", "/dev/stdout", "&&", "echo", "* * * * * /bin/sh /app/your_script.sh >/dev/null 2>&1", ">>", "/etc/crontabs/root"]
