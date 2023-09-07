FROM python:3.9-bullseye

ENV IBMI_VERSION="1.1.0"

# Install IBM IAccess
RUN set -ex \
    && curl "https://public.dhe.ibm.com/software/ibmi/products/odbc/debs/dists/${IBMI_VERSION}/ibmi-acs-${IBMI_VERSION}.list" \
      | tee "/etc/apt/sources.list.d/ibmi-acs-${IBMI_VERSION}.list" \
    && apt-get update \
    && apt-get install -y ibm-iaccess \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf "/etc/apt/sources.list.d/ibmi-acs-${IBMI_VERSION}.list"

RUN mkdir -p /opt/app

RUN pip install pyodbc iseries django pytest-django

COPY . /opt/app

WORKDIR /opt/app

RUN python setup.py develop

CMD ["bash", "-c", "pytest"]
