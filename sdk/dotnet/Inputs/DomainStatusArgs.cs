// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Inputs
{

    public sealed class DomainStatusArgs : global::Pulumi.ResourceArgs
    {
        [Input("dnsConfigs")]
        private InputList<Inputs.DomainStatusDnsConfigArgs>? _dnsConfigs;
        public InputList<Inputs.DomainStatusDnsConfigArgs> DnsConfigs
        {
            get => _dnsConfigs ?? (_dnsConfigs = new InputList<Inputs.DomainStatusDnsConfigArgs>());
            set => _dnsConfigs = value;
        }

        [Input("endpoints")]
        private InputList<Inputs.DomainStatusEndpointArgs>? _endpoints;
        public InputList<Inputs.DomainStatusEndpointArgs> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<Inputs.DomainStatusEndpointArgs>());
            set => _endpoints = value;
        }

        [Input("fingerprint")]
        public Input<string>? Fingerprint { get; set; }

        [Input("locations")]
        private InputList<Inputs.DomainStatusLocationArgs>? _locations;
        public InputList<Inputs.DomainStatusLocationArgs> Locations
        {
            get => _locations ?? (_locations = new InputList<Inputs.DomainStatusLocationArgs>());
            set => _locations = value;
        }

        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("warning")]
        public Input<string>? Warning { get; set; }

        public DomainStatusArgs()
        {
        }
        public static new DomainStatusArgs Empty => new DomainStatusArgs();
    }
}