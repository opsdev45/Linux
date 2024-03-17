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

# Add the cron job
RUN echo "* * * * * /bin/sh /app/log_err.sh >/dev/null 2>&1" >> /etc/crontabs/root

# Run cron in the foreground
CMD ["crond", "-f", "-d", "8", "-l", "8", "-L", "/dev/stdout"]
