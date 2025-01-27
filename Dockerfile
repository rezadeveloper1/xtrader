# Use the official Python image
FROM python:3.9
LABEL maintainer="dc.ramzservat.com"

# Set the working directory
WORKDIR /xtrader

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:/py/bin:$PATH"

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libxml2 \
    libxml2-dev \
    libxslt1-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    postgresql-client \
    wget \
    vim \
    less

# Download and build TA-Lib
RUN wget https://github.com/ta-lib/ta-lib/releases/download/v0.6.2/ta-lib_0.6.2_amd64.deb && \ 
    dpkg -i ta-lib_0.6.2_amd64.deb && \
    rm ta-lib_0.6.2_amd64.deb
RUN pip install ta-lib


# Copy the requirements file and project code
COPY ./requirements.txt /xtrader/

# Create and activate a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

# Install project dependencies
RUN /py/bin/pip install --no-cache-dir --progress-bar on --default-timeout=2000 --retries=10 -r /xtrader/requirements.txt

# Clean up unnecessary packages
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY ./xtrader /xtrader/
COPY ./scripts /scripts

# Create a non-root user and set up directories
RUN adduser --disabled-password --no-create-home xtrader
RUN mkdir -p /vol/web/static /vol/web/media
RUN chown -R xtrader:xtrader /xtrader /vol
RUN chmod -R 755 /vol
RUN chmod -R +x /scripts

# Switch to the non-root user
USER xtrader

# Expose the port
EXPOSE 9000

# Specify the default command to run on container start
CMD ["run.sh"]
