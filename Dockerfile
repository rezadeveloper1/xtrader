# Use the official Python image
FROM python:3.9
LABEL maintainer="dc.ramzservat.com"

# Set the working directory
WORKDIR /xtrader

# Set environment variables
ENV PYTHONUNBUFFERED 1
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
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xvzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure --prefix=/usr --build=aarch64-unknown-linux-gnu && \
    make && \
    make install && \
    cd .. && \
    rm -rf ta-lib ta-lib-0.4.0-src.tar.gz

# Copy the requirements file and project code
COPY ./requirements.txt /xtrader/

# Create and activate a virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip

# Install project dependencies
RUN /py/bin/pip install -r /xtrader/requirements.txt

# Clean up unnecessary packages
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY ./xtrader /xtrader/
COPY ./scripts /scripts

# Create a non-root user and set up directories
RUN adduser --disabled-password --no-create-home xtrader && \
    mkdir -p /vol/web/static /vol/web/media && \
    chown -R xtrader:xtrader /xtrader /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

# Switch to the non-root user
USER xtrader

# Expose the port
EXPOSE 9000

# Specify the default command to run on container start
CMD ["run.sh"]
